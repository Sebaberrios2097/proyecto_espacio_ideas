# Generated by Django 4.2 on 2023-07-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_producto_personalizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion_corta',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]