from django.db import models
from django.contrib.auth.models import User

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, verbose_name='Usuario')
    fono = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user.username

    