import json
from datetime import date
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Count
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from dealflow.app.crm.forms import AccountForm, OpportunityForm, ProspectForm
from dealflow.app.crm.models import Account, Activity, Opportunity, Pipeline, Prospect


class DashboardView(LoginRequiredMixin, ListView):
    template_name = "crm/dashboard.html"
    context_object_name = "accounts"

    def get_queryset(self):
        if self.request.user.role.upper() == "ADMIN":
            return Account.objects.all()
        else:
            return Account.objects.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_activity = None
        total_account_data = None
        total_opportunity = None

        if self.request.user.role.upper() == "ADMIN":
            total_activity = Activity.objects.get_admin_activity_data()
            total_account_data = Account.objects.get_admin_total_account()
            total_opportunity = Opportunity.objects.get_admin_total_opportunity()

        else:
            total_activity = Activity.objects.get_user_activity_data(self.request.user)
            total_account_data = Account.objects.get_total_account(self.request.user)
            total_opportunity = Opportunity.objects.get_total_opportunity(self.request.user)

        order_activity_data = []
        for month in range(1, 13):
            order_activity_data.append(total_activity.get(month, 0))

        print(total_opportunity)
            
        context["activity_data"] = json.dumps(order_activity_data)
        context["total_account_data"] = total_account_data
        context["total_opportunity"] = total_opportunity

        return context
    

class AdminAccountView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "crm/admin/account.html"
    # permission_denied_url = reverse_lazy('crm:dashboard')
    # raise_exception = False

    def test_func(self):
        return self.request.user.role.upper() == 'ADMIN'

    def get(self, request):
        accounts = Account.objects.all()
        print(accounts)
        return render(request, self.template_name, {'admin_accounts': accounts})
    

class AccountView(LoginRequiredMixin, View):
    template_name = "crm/account.html"

    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        prospect = None

        for account in accounts:
            prospect = Prospect.objects.filter(account=account)
            print("prospect : ", prospect)
        return render(request, self.template_name, {'accounts': accounts, 'prospect': prospect})
    

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = "crm/account_form.html"
    success_url = reverse_lazy('admin_account')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.status = "Prospect"
        self.object.save()

        messages.success(self.request, "Compte crée avec success.")

        return super().form_valid(form)


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = "crm/account_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.objects.filter(user=self.request.user)
        return context
    

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = "crm/account_form.html"
    success_url = reverse_lazy("account")

    def form_valid(self, form):
        messages.success(self.request, "Compte modifier avec success.")
        return super().form_valid(form)
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Account, pk=pk)

class ProspectView(LoginRequiredMixin, View):
    template_name = "crm/prospect.html"

    def get(self, request):
        prospects = Prospect.objects.filter(user=request.user)
        return render(request, self.template_name, {'prospects': prospects})


class ProspectCreateView(LoginRequiredMixin, CreateView):
    model = Prospect
    form_class = ProspectForm
    template_name = "crm/prospect_form.html"
    success_url = reverse_lazy("prospect")

    def form_valid(self, form):
        account_pk = self.kwargs.get('account_id')
        print("account_id : ", account_pk)
        account = get_object_or_404(Account, pk=account_pk)

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.account = account

        self.object.save()

        messages.success(self.request, f"Le prospect {self.object.first_name} à été crée avec success sur le compte {self.object.account.account_name}")

        return super().form_valid(form)
    

class ProspectUpdateView(LoginRequiredMixin, UpdateView):
    model = Prospect
    form_class = ProspectForm
    template_name = "crm/prospect_form.html"
    success_url = reverse_lazy("prospect")

    def form_valid(self, form):
        messages.success(self.request, "Prospect modifié avec succès.")
        return super().form_valid(form)


class ProspectDeleteView(LoginRequiredMixin, DeleteView):
    model = Prospect
    template_name = "crm/prospect_delete.html"
    success_url = reverse_lazy("prospect")

    def delete(self, request, *args, **kwargs):
        message = super().delete(request, *args, **kwargs)
        messages.success(request, f"Prospect supprimé avec success.")
        return message
    

class ServiceView(LoginRequiredMixin, View):
    template_name = "crm/service.html"

    def get(self, request):
        return render(request, self.template_name)
    

class OpportunityView(LoginRequiredMixin, ListView):
    template_name = "crm/opportunity.html"
    context_object_name = 'opportunities'
    
    def get_queryset(self):
        if self.request.user.role.upper() == "ADMIN":
            return Opportunity.objects.all()
        else:
            return Opportunity.objects.filter(user=self.request.user)
    

class OpportunityCreateView(LoginRequiredMixin, CreateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = "crm/opportunity_form.html"
    success_url = reverse_lazy("opportunity")
    
    def form_valid(self, form):
        prospect_pk = self.kwargs.get('pk')
        prospect = get_object_or_404(Prospect, pk=prospect_pk)
        print("prospect : ", prospect.account.id)
        account = get_object_or_404(Account, pk=prospect.account.id)

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.account = account
        self.object.prospect = prospect

        try:
            initial_step = get_object_or_404(Pipeline, step_name="Qualification")
        except Pipeline.DoesNotExist:
            messages.error(self.request, "Erreur : L'étape de pipeline initiale 'Qualification' n'a pas été trouvée. Veuillez contacter l'administrateur.")
            return self.form_invalid(form)
        
        self.object.pipeline = initial_step

        self.object.save()

        messages.success(self.request, f"Opportunité à été crée avec success sur le compte {self.object.account.account_name}")

        return super().form_valid(form)
    

class ActivityView(LoginRequiredMixin, View):
    template_name = "crm/activity.html"

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        return render(request, self.template_name, {'activities': activities})
    

class ActivityCreateView(LoginRequiredMixin, View):
    template_name = "crm/activity_form.html"

    def get(self, request):
        return render(request, self.template_name)