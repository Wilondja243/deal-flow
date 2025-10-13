from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from dealflow.app.crm.forms import AccountForm, ProspectForm
from dealflow.app.crm.models import Account, Activity, Prospect


class DashboardView(LoginRequiredMixin, View):
    template_name = "crm/dashboard.html"

    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        return render(request, self.template_name, {'accounts': accounts})
    

class AccountView(LoginRequiredMixin, View):
    template_name = "crm/account.html"

    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        return render(request, self.template_name, {'accounts': accounts})
    

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = "crm/account_form.html"
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.status = "Prospect"
        self.object.save()

        print("Formulaire réussi")

        return super().form_valid(form)


class AccountDeatailView(LoginRequiredMixin, DetailView):
    pass


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
    

class ProductView(LoginRequiredMixin, View):
    template_name = "crm/product.html"

    def get(self, request):
        return render(request, self.template_name)
    

class OpportunityView(LoginRequiredMixin, View):
    template_name = "crm/opportunity.html"

    def get(self, request):
        return render(request, self.template_name)
    

class ActivityView(LoginRequiredMixin, View):
    template_name = "crm/activity.html"

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        return render(request, self.template_name, {'activities': activities})
    

class ActivityCreateView(LoginRequiredMixin, View):
    template_name = "crm/activity_form.html"

    def get(self, request):
        return render(request, self.template_name)