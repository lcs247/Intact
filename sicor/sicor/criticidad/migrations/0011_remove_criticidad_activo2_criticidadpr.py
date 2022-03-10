# Generated by Django 4.0 on 2022-03-06 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0027_alter_planta_descripcion_and_more'),
        ('criticidad', '0010_criticidad_activo2_alter_criticidad_activo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criticidad',
            name='activo2',
        ),
        migrations.CreateModel(
            name='CriticidadPr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?')),
                ('ps', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN SISTEMA?')),
                ('fua', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?')),
                ('pe', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?')),
                ('sh', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?')),
                ('ma', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?')),
                ('r', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='REDUNDANCIA')),
                ('crit_pacial', models.FloatField(default=0.0, verbose_name='CRITICIDAD PARCIAL')),
                ('eval_redun', models.PositiveIntegerField(default=0.0, verbose_name='EVAL REDUNDANCIA')),
                ('crit_total', models.FloatField(default=0.0, verbose_name='CRITICIDAD TOTAL')),
                ('ingres', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal')),
            ],
        ),
    ]