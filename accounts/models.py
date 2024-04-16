
import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key