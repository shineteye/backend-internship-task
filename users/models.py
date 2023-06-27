from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        unique=True, blank=True, max_length=50)
    email = models.EmailField(
        unique=True, max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    number_of_calories = models.OneToOneField(
        to=User, on_delete=models.PROTECT)
