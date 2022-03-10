# Generated by Django 4.0 on 2022-03-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criticidad', '0013_costo_exposicion_mda_ocurrencia_perdida_redundancia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costo',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exposicion',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mda',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ocurrencia',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perdida',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='redundancia',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='segysa',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
