# Generated by Django 4.2 on 2023-07-14 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0019_alter_pedido_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='transaction_id',
            field=models.CharField(default='6398388664', max_length=100),
        ),
    ]