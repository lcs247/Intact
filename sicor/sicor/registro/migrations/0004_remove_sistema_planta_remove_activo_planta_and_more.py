# Generated by Django 4.0 on 2022-01-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_sistema_planta_alter_activo_planta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistema',
            name='planta',
        ),
        migrations.RemoveField(
            model_name='activo',
            name='planta',
        ),
        migrations.AddField(
            model_name='activo',
            name='planta',
            field=models.ManyToManyField(to='registro.Planta'),
        ),
        migrations.RemoveField(
            model_name='activo',
            name='sistema',
        ),
        migrations.AddField(
            model_name='activo',
            name='sistema',
            field=models.ManyToManyField(to='registro.Sistema'),
        ),
    ]
