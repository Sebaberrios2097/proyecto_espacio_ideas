# Generated by Django 4.2 on 2023-07-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='carrusel')),
                ('encabezado', models.CharField(max_length=50)),
                ('subencabezado', models.CharField(max_length=350)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Carrusel',
                'verbose_name_plural': 'Carrusel',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
