from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fono = models.CharField(max_length=12, null=True, blank=True)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    pass

    # cambia los nombres de los accesos inversos para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_custom',
        blank=True,
        help_text='Los permisos específicos de este usuario.'
    )
