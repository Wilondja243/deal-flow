from django.urls import path

from dealflow.app.crm.views import (
    DashboardView,
    OpportunityView,
    ProspectView,
    ProspectCreateView,
    ProductView,
    AccountView,
    AccountCreateView,
    ActivityView,
)


urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('opportunity/', OpportunityView.as_view(), name="opportunity"),
    path('prospect/', ProspectView.as_view(), name="prospect"),
    path('prospect/create/', ProspectCreateView.as_view(), name="prospect_create"),
    path('product/', ProductView.as_view(), name="product"),
    path('account/', AccountView.as_view(), name="account"),
    path('account/create/', AccountCreateView.as_view(), name="account_create"),
    path('activity/', ActivityView.as_view(), name="activity"),
]