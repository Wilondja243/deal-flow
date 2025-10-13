from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from dealflow.app.crm.forms import AccountForm, ProspectForm
from dealflow.app.crm.models import Account, Prospect


class DashboardView(LoginRequiredMixin, View):
    template_name = "crm/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)
    

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
    


class ProspectView(LoginRequiredMixin, View):
    template_name = "crm/prospect.html"

    def get(self, request):
        return render(request, self.template_name)


class ProspectCreateView(LoginRequiredMixin, CreateView):
    model = Prospect
    form_class = ProspectForm
    template_name = "crm/prospect_form.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        account_pk = self.kwargs.get('pk')
        account = get_object_or_404(Account, pk=account_pk)

        form = form.save(commit=False)
        form.user = self.request.user
        form.account = account

        return super().form_valid(form)
    

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
        return render(request, self.template_name)
    

class ActivityCreateView(LoginRequiredMixin, View):
    template_name = "crm/activity_form.html"

    def get(self, request):
        return render(request, self.template_name)