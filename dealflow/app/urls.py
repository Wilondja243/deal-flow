from django.urls import path

from dealflow.app.crm.views import (
    DashboardView,
    OpportunityView,
    ProspectView,
    ProductView
)


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('opportunity/', OpportunityView.as_view(), name="opportunity"),
    path('prospect/', ProspectView.as_view(), name="prospect"),
    path('product/', ProductView.as_view(), name="product")
]