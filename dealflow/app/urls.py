from django.urls import path

from dealflow.app.crm.views import DashboardView, OpportunityView


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('opportunity/', OpportunityView.as_view(), name="opportunity"),
]