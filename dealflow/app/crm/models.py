
from uuid import uuid4
from django.db import models
from django.conf import settings

from dealflow.app.core.models import BaseModel


class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()


class Account(BaseModel):
    STATUS_CHOICES = [
        ('Prospect', 'Prospect'),
        ('Active_Client', 'Active Client'),
        ('Former_Client', 'Former Client'),
        ('Partner', 'Partner'),
        ('Archived', 'Archived'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    activity_sector = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Prospect")


class Prospect(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


class Pipeline(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    step_name = models.CharField(max_length=100)
    display_order = models.IntegerField()
    is_closed = models.BooleanField(default=False)


class Opportunity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    deal_name = models.CharField(max_length=100)
    estimate_value = models.DecimalField(max_digits=8, decimal_places=2)
    cloture_data = models.DateTimeField(null=True, blank=True)


class Activity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    description_note = models.TextField()
    is_finished = models.BooleanField(default=False)