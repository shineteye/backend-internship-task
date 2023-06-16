from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


def create_superuser(self, email, username, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    return self.create_user(email, username, password, **extra_fields)


# Custom user model with email as unique identifier
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Fields for expected number of calories per day
    expected_calories_per_day = models.PositiveIntegerField(default=2000)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# Model for each entry


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Entry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()
    calories = models.PositiveIntegerField(null=True)
    is_below_expected = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.date}'

    class Meta:
        ordering = ['-date', '-time']
        verbose_name_plural = 'Entry'
