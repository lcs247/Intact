# Generated by Django 4.0 on 2022-03-08 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0027_alter_planta_descripcion_and_more'),
        ('criticidad', '0016_criticidadcpr_nombre_criticidadcsec_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criticidadcpr',
            name='activo',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal'),
        ),
        migrations.AlterField(
            model_name='criticidadcpr',
            name='ctdr',
            field=models.CharField(default='?', max_length=30, verbose_name='CATEGORÍA DE RIESGO'),
        ),
    ]
