# Generated by Django 4.2 on 2023-04-29 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_remove_detallepedido_personalizacion_predefinida'),
        ('personalizacion', '0008_personalizacionpredefinida_mensaje_personalizado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenpersonalizacion',
            name='persoPredefinida',
        ),
        migrations.AlterField(
            model_name='imagenpersonalizacion',
            name='personalizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalizacion.personalizacion'),
        ),
        migrations.DeleteModel(
            name='PersonalizacionPredefinida',
        ),
    ]
