# Generated by Django 4.0 on 2022-03-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criticidad', '0011_remove_criticidad_activo2_criticidadpr'),
    ]

    operations = [
        migrations.AddField(
            model_name='criticidad',
            name='nombre',
            field=models.CharField(blank=True, default='????', max_length=70),
        ),
        migrations.AddField(
            model_name='criticidadpr',
            name='nombre',
            field=models.CharField(blank=True, default='????', max_length=70),
        ),
    ]
