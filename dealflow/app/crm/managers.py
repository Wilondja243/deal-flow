from datetime import date
from django.db import models
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth


class AccountManager(models.Manager):

    def get_admin_total_account(self):
        return self.aggregate(
            total=Count('id'),
            total_users = Count('user__id', distinct=True),
        )
    
    def get_total_account(self, user):
        return self.filter(user=user).aggregate(total=Count('id'))
    

class OpportunityManager(models.Manager):

    def get_admin_total_opportunity(self):
        return self.aggregate(
            total=Count('id'),
            total_value=Sum('estimate_value')
        )
    
    def get_total_opportunity(self, user):
        return self.filter(user=user).aggregate(
            total=Count('id'),
            total_value=Sum('estimate_value')
        )
    

class ActivityManager(models.Manager):

    def get_admin_activity_data(self):
        activity_data = self.filter(
            created_at__year = date.today().year,
        ).annotate(month=ExtractMonth("created_at")).values('month').annotate(
            total=Count('id')
        )
        total_activity = {item['month']: item['total_activities'] for item in activity_data}

        return total_activity
    
    def get_user_activity_data(self, user):
        activity_data = self.filter(
            created_at__year = date.today().year,
            user=user
        ).annotate(month=ExtractMonth("created_at")).values('month').annotate(
            total=Count('id')
        )
        total_activity = {item['month']: item['total_activities'] for item in activity_data}

        return total_activity
    