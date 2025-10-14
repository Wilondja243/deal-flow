from django.urls import path

from dealflow.app.users.views import LoginView, SignupView, LogoutView
from dealflow.app.crm.views import (
    DashboardView,
    OpportunityView,
    ProspectView,
    ProspectCreateView,
    ProspectDeleteView,
    ProspectUpdateView,
    ProductView,
    AdminAccountView,
    AccountView,
    AccountCreateView,
    AccountUpdateView,
    ActivityView,
    ActivityCreateView,
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
    path('dashboard/prospect/', ProspectView.as_view(), name="prospect"),
    path('dashboard/prospect/<uuid:account_id>/', ProspectCreateView.as_view(), name="prospect_create"),
    path('dashboard/prospect/<uuid:pk>/update/', ProspectUpdateView.as_view(), name="prospect_update"),
    path('dashboard/prospect/<uuid:pk>/delete/', ProspectDeleteView.as_view(), name="prospect_delete"),
    path('dashboard/product/', ProductView.as_view(), name="product"),
    path('dashboard/activity/', ActivityView.as_view(), name="activity"),
    path('dashboard/activity/create/', ActivityCreateView.as_view(), name="activity_create"),
]