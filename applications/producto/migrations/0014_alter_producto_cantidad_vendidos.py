# Generated by Django 4.2 on 2023-07-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0013_producto_cantidad_vendidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad_vendidos',
            field=models.IntegerField(default=0),
        ),
    ]
