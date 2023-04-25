from django.db import models

class UserExtra(models.Model):
    fono = models.CharField(max_length=12, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)

    