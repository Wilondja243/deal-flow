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


class ProspectView(View):
    template_name = "crm/prospect.html"

    def get(self, request):
        return render(request, self.template_name)
    

class ProductView(View):
    template_name = "crm/product.html"

    def get(self, request):
        return render(request, self.template_name)