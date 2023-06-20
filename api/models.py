from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, blank=True, max_length=50)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    text = models.TextField()
    number_of_calories = models.IntegerField()
    is_calories_less_than_expected = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Entries'
