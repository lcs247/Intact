# Generated by Django 4.0 on 2022-01-23 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0013_equipo_codes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='codes',
        ),
        migrations.AddField(
            model_name='equipo',
            name='codigo_unico',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='estado',
            field=models.CharField(choices=[('O', 'Operativo'), ('F', 'Fuera de Servicio')], default='O', max_length=9, verbose_name='Estado Operativo'),
        ),
    ]
