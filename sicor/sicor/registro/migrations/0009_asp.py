# Generated by Django 4.0 on 2022-01-22 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_remove_sistema_planta_sistema_planta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.activo')),
                ('planta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.planta')),
                ('sistema', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.sistema')),
            ],
        ),
    ]
