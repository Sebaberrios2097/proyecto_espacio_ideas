# Generated by Django 4.2 on 2023-07-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0006_alter_pedido_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='transaction_id',
            field=models.CharField(default='2903254353', max_length=100),
        ),
    ]