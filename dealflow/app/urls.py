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
    path('account/', AccountView.as_view(), name="account"),
    path('account/create/', AccountCreateView.as_view(), name="account_create"),
    path('account/<uuid:pk>/update/', AccountUpdateView.as_view(), name="account_update"),
    path('opportunity/', OpportunityView.as_view(), name="opportunity"),
    path('prospect/', ProspectView.as_view(), name="prospect"),
    path('prospect/<uuid:account_id>/', ProspectCreateView.as_view(), name="prospect_create"),
    path('prospect/<uuid:pk>/update/', ProspectUpdateView.as_view(), name="prospect_update"),
    path('prospect/<uuid:pk>/delete/', ProspectDeleteView.as_view(), name="prospect_delete"),
    path('product/', ProductView.as_view(), name="product"),
    path('activity/', ActivityView.as_view(), name="activity"),
    path('activity/create/', ActivityCreateView.as_view(), name="activity_create"),
]