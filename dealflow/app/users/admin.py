from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'is_superuser', 'is_active', 'role']
    list_filter = ['username', 'email', 'role', 'is_active']


admin.site.register(User, UserAdmin)
