from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('user','User'),
        ('admin','Admin')
    )
    role = models.CharField(max_length=10, choices=ROLES, default='admin')
    first_name=models.CharField(max_length=100, blank=True)
    last_name=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.username}"
