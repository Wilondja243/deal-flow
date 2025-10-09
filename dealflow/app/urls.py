from django.urls import path

from dealflow.app.crm.views import DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard")
]