from django.urls import path

from dealflow.app.users.views import LoginView, SignupView, LogoutView
from dealflow.app.crm.views import (
    DashboardView,
    OpportunityView,
    OpportunityCreateView,
    OpportunityUpdateView,
    OpportunityDeleteView,
    ProspectView,
    ProspectCreateView,
    ProspectDeleteView,
    ProspectUpdateView,
    ServiceView,
    AdminAccountView,
    AccountView,
    AccountCreateView,
    AccountUpdateView,
    ActivityView,
    ActivityCreateView,
    ActivityUpdateView,
    ActivityDeleteView,
)


urlpatterns = [
    path('account/login/', LoginView.as_view(), name="login"),
    path('account/create_user/', SignupView.as_view(), name="create_user"),
    path('account/logout/', LogoutView.as_view(), name="logout"),

    path('', DashboardView.as_view(), name="dashboard"),
    path('admin/account/', AdminAccountView.as_view(), name="admin_account"),
    path('account/create/', AccountCreateView.as_view(), name="account_create"),
    path('account/<uuid:pk>/update/', AccountUpdateView.as_view(), name="account_update"),
    path('dashboard/account/', AccountView.as_view(), name="account"),
    path('dashboard/opportunity/', OpportunityView.as_view(), name="opportunity"),
    path('dashboard/opportunity/<uuid:pk>/create/', OpportunityCreateView.as_view(), name="opportunity_create"),
    path('dashboard/opportunity/<uuid:pk>/update', OpportunityUpdateView.as_view(), name="opportunity_update"),
    path('dashboard/opportunity/<uuid:pk>/delete/', OpportunityDeleteView.as_view(), name="opportunity_delete"),
    path('dashboard/prospect/', ProspectView.as_view(), name="prospect"),
    path('dashboard/prospect/<uuid:account_id>/', ProspectCreateView.as_view(), name="prospect_create"),
    path('dashboard/prospect/<uuid:pk>/update/', ProspectUpdateView.as_view(), name="prospect_update"),
    path('dashboard/prospect/<uuid:pk>/delete/', ProspectDeleteView.as_view(), name="prospect_delete"),
    path('dashboard/service/', ServiceView.as_view(), name="service"),
    path('dashboard/activity/', ActivityView.as_view(), name="activity"),
    path('dashboard/activity/<uuid:opportunity_id>/create/', ActivityCreateView.as_view(), name="activity_create"),
    path('dashboard/<uuid:pk>/update/', ActivityUpdateView.as_view(), name="activity_update"),
    path('dashboard/<uuid:pk>/delete/', ActivityDeleteView.as_view(), name="activity_delete"),
]