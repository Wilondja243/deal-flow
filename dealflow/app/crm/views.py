from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    template_name = "crm/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)


class OpportunityView(LoginRequiredMixin, View):
    template_name = "crm/opportunity.html"

    def get(self, request):
        return render(request, self.template_name)


class ProspectView(LoginRequiredMixin, View):
    template_name = "crm/prospect.html"

    def get(self, request):
        return render(request, self.template_name)


class ProspectCreateView(LoginRequiredMixin, View):
    template_name = "crm/prospect_form.html"

    def get(self, request):
        return render(request, self.template_name)
    

class ProductView(LoginRequiredMixin, View):
    template_name = "crm/product.html"

    def get(self, request):
        return render(request, self.template_name)
    

class AccountView(LoginRequiredMixin, View):
    template_name = "crm/account.html"

    def get(self, request):
        return render(request, self.template_name)
    

class AccountCreateView(LoginRequiredMixin, View):
    template_name = "crm/account_form.html"

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