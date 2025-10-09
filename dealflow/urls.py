
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Système de Gestion DealFlow"
admin.site.site_title = "DealFlow Admin"
admin.site.index_title = "Gestion DealFlow"

urlpatterns = [
    path('dealflow/admin/', admin.site.urls),

    path("", include('dealflow.app.urls'))
]
