# Generated by Django 4.0 on 2022-01-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='observaciones',
            field=models.CharField(max_length=100, verbose_name='Observaciones'),
        ),
    ]
