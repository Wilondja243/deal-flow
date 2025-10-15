from django.contrib import admin

from .models import (
    Service,
    Account,
    Pipeline,
)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'price', 'description', 'created_at', 'update_at']
    list_filter = ['service_name', 'created_at']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_name', 'address', 'activity_sector', 'status']
    list_filter = ['account_name', 'address', 'activity_sector', 'status']


class PipelineAdmin(admin.ModelAdmin):
    list_display = ['step_name', 'display_order', 'is_closed']
    list_filter = ['step_name', 'is_closed']


admin.site.register(Service, ServiceAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Pipeline, PipelineAdmin)