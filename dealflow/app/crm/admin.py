from django.contrib import admin

from .models import (
    Product,
    Account,
    Pipeline,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'description', 'created_at', 'update_at']
    list_filter = ['product_name', 'created_at']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'address', 'activity_sector', 'status']
    list_filter = ['company_name', 'address', 'activity_sector', 'status']


class PipelineAdmin(admin.ModelAdmin):
    list_display = ['step_name', 'display_order', 'is_closed']
    list_filter = ['step_name', 'is_closed']


admin.site.register(Product, ProductAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Pipeline, PipelineAdmin)