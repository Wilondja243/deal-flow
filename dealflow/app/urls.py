from django.urls import path

from dealflow.app.users.views import LoginView
from dealflow.app.crm.views import (
    DashboardView,
    OpportunityView,
    ProspectView,
    ProspectCreateView,
    ProductView,
    AccountView,
    AccountCreateView,
    ActivityView,
    ActivityCreateView,
)


urlpatterns = [
    path('account/login/', LoginView.as_view(), name="login"),

    path('', DashboardView.as_view(), name="dashboard"),
    path('opportunity/', OpportunityView.as_view(), name="opportunity"),
    path('prospect/', ProspectView.as_view(), name="prospect"),
    path('prospect/create/', ProspectCreateView.as_view(), name="prospect_create"),
    path('product/', ProductView.as_view(), name="product"),
    path('account/', AccountView.as_view(), name="account"),
    path('account/create/', AccountCreateView.as_view(), name="account_create"),
    path('activity/', ActivityView.as_view(), name="activity"),
    path('activity/create/', ActivityCreateView.as_view(), name="activity_create"),
]