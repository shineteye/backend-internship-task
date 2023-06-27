from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # auth.User


class Entry(models.Model):
    user = models.ForeignKey(
        User,  default=1,  null=True, related_name='entries', on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    text = models.TextField()
    number_of_calories = models.IntegerField()
    is_calories_less_than_expected = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Entries'
