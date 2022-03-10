# Generated by Django 4.0 on 2022-01-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_remove_activo_planta_remove_sistema_planta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistema',
            name='planta',
        ),
        migrations.AddField(
            model_name='sistema',
            name='planta',
            field=models.ManyToManyField(to='registro.Planta'),
        ),
    ]
