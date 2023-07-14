from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    fono = models.CharField(max_length = 20, blank = True)
    insta = models.CharField(max_length = 30, blank = True)
    facebook = models.CharField(max_length = 30, blank = True)
    twitter = models.CharField(max_length = 30, blank = True)

    def __str__(self):
        return "Perfil de " + self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender = User)
post_save.connect(save_user_profile, sender = User)