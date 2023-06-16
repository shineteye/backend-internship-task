from django.db import models
from django.contrib.auth import get_user_model
from users.models import User


class Calories(models.Model):
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField(max_length=255)
    number_of_calories = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_total_less_than_expected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} by {self.created_by}"

    class Meta:
        verbose_name_plural = 'Calories'
