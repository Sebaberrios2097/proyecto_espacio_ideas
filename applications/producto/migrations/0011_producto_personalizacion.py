# Generated by Django 4.2 on 2023-04-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalizacion', '0010_remove_personalizacion_producto'),
        ('producto', '0010_producto_aviso'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='personalizacion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personalizacion.personalizacion'),
        ),
    ]
