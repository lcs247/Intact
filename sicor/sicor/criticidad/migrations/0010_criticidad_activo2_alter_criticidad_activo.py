# Generated by Django 4.0 on 2022-03-06 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0027_alter_planta_descripcion_and_more'),
        ('criticidad', '0009_alter_criticidad_crit_pacial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='criticidad',
            name='activo2',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='criticidad',
            name='activo',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='registro.equipo'),
        ),
    ]
