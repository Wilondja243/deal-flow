from django.shortcuts import render
from django.views.generic import View


class DashboardView(View):
    template_name = "crm/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)


class OpportunityView(View):
    template_name = "crm/opportunity.html"

    def get(self, request):
        return render(request, self.template_name)