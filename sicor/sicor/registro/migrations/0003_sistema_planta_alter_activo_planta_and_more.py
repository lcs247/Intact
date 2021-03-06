# Generated by Django 4.0 on 2022-01-22 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_activo_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='planta',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registro.planta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activo',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.planta'),
        ),
        migrations.AlterField(
            model_name='activo',
            name='sistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.sistema'),
        ),
    ]
