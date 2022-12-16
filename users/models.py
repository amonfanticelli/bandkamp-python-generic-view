from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        ordering = ["id"]

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_superuser = models.BooleanField()
