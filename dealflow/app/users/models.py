from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOISES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('commercial', 'Commercial'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOISES)
