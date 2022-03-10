# Generated by Django 4.0 on 2022-02-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0020_alter_equipo_codes'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='datasheet',
            field=models.FileField(blank=True, upload_to='datasheets/'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='año',
            field=models.DateField(blank=True, verbose_name='Año de fabricación'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='capacidad',
            field=models.CharField(blank=True, max_length=70, verbose_name='Capacidad de Diseño/Operativa'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='estado',
            field=models.CharField(choices=[('O', 'Operativo'), ('F', 'Fuera de Servicio')], default='Operativo', max_length=9, verbose_name='Estado Operativo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fu_mantenimiento',
            field=models.DateField(blank=True, verbose_name='Fecha de último mantenimiento integral'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='observaciones',
            field=models.CharField(blank=True, max_length=100, verbose_name='Observaciones'),
        ),
    ]
