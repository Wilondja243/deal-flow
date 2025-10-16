
from uuid import uuid4
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from .managers import ActivityManager, AccountManager, OpportunityManager
from dealflow.app.core.models import BaseModel


class Service(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    service_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


class Account(BaseModel):
    STATUS_CHOICES = [
        ('Prospect', 'Prospect'),
        ('Active_Client', 'Active Client'),
        ('Archived', 'Archived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    account_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    activity_sector = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    account_phone_number = PhoneNumberField(unique=True, region="FR")
    web_site = models.URLField(null=True, blank=True)
    postal_code = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Prospect")


    objects = AccountManager()


class Prospect(BaseModel):
    STATUS_CHOICES = [
        ('Prospect', 'Prospect'),
        ('Client', 'Active'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="prospect")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="prospect")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True, region="FR")
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default="Prospect")


class Pipeline(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    step_name = models.CharField(max_length=100)
    display_order = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_closed = models.BooleanField(default=False, null=True, blank=True)


class Opportunity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    prospect = models.ForeignKey(Prospect, on_delete=models.SET_NULL, null=True)
    deal_name = models.CharField(max_length=100)
    estimate_value = models.DecimalField(max_digits=8, decimal_places=2)
    cloture_date = models.DateTimeField(null=True, blank=True)
    probability_purcent = models.CharField(max_length=20, default="")


    objects = OpportunityManager()


class Activity(BaseModel):
    RESULT_CHOICES = [
        ("SCHEDULED", "Planifié / À venir"),
        ("COMPLETED_SUCCESS", "Terminé / Réussi"),
        ("NO_RESPONSE", "Pas de réponse / Message envoyé"),
        ("COMPLETED_FAILED", "Terminé / Non abouti"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=RESULT_CHOICES, default="SCHEDULED")
    description_note = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)

    objects = ActivityManager()