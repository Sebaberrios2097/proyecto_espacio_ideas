# Generated by Django 4.2 on 2023-04-25 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalizacion', '0003_remove_personalizacion_img_perso_delete_imgperso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalizacion',
            name='user',
        ),
    ]
