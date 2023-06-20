from django.db import models
from users.models import User


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
