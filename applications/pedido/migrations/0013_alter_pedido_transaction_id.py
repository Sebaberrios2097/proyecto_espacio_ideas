# Generated by Django 4.2 on 2023-07-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0012_alter_pedido_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='transaction_id',
            field=models.CharField(default='0952287400', max_length=100),
        ),
    ]