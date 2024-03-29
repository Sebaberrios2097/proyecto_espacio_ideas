# Generated by Django 4.2 on 2023-04-29 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_alter_producto_fecha_creacion_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personalizacion', '0007_personalizacionpredefinida_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizacionpredefinida',
            name='mensaje_personalizado',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalizacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalizacionpredefinida',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto'),
        ),
    ]
