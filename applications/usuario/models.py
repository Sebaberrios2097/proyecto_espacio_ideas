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

# Otra forma de crear un usuario de django
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('El email es requerido')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(email=email, password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     nombre = models.CharField(max_length=100)
#     apellidos = models.CharField(max_length=100)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     es_activo = models.BooleanField(default=True)
#     es_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['nombre', 'apellidos']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.es_staff

#     @property
#     def is_active(self):
#         return self.es_activo
