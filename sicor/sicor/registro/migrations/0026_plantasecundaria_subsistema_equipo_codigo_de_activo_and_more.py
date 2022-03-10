# Generated by Django 4.0 on 2022-03-04 00:31

from django.db import migrations, models
import django.db.models.deletion
import registro.models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0025_alter_equipo_datasheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantaSecundaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Planta')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=70, verbose_name='Descripción')),
                ('capacidad', models.CharField(blank=True, max_length=40, verbose_name='Capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='SubSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Sistema')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=70, verbose_name='Descripción')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='codigo_de_activo',
            field=models.CharField(blank=True, max_length=20, verbose_name='Código de activo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='fases',
            field=models.CharField(blank=True, max_length=20, verbose_name='Nro. de Fases'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.CharField(blank=True, max_length=20, verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='modelo',
            field=models.CharField(blank=True, max_length=20, verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='potencia',
            field=models.CharField(blank=True, max_length=20, verbose_name='Potencia'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='presion',
            field=models.CharField(blank=True, max_length=20, verbose_name='Presión descarga'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='producto',
            field=models.CharField(blank=True, max_length=20, verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='serie',
            field=models.CharField(blank=True, max_length=20, verbose_name='Serie'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='temperatura',
            field=models.CharField(blank=True, max_length=20, verbose_name='Temperatura'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='tipo',
            field=models.CharField(blank=True, max_length=20, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='voltaje',
            field=models.CharField(blank=True, max_length=20, verbose_name='Voltaje'),
        ),
        migrations.AddField(
            model_name='planta',
            name='capacidad',
            field=models.CharField(blank=True, max_length=40, verbose_name='Capacidad'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='año',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de instalación'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=70, verbose_name='Descripción'),
        ),
        migrations.CreateModel(
            name='EquipoPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(max_length=70, verbose_name='Descripción')),
                ('codes', models.CharField(blank=True, default='????', max_length=70)),
                ('marca', models.CharField(blank=True, max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=20, verbose_name='Modelo')),
                ('serie', models.CharField(blank=True, max_length=20, verbose_name='Serie')),
                ('tipo', models.CharField(blank=True, max_length=20, verbose_name='Tipo')),
                ('codigo_de_activo', models.CharField(blank=True, max_length=20, verbose_name='Código de activo')),
                ('año', models.DateField(blank=True, null=True, verbose_name='Fecha de instalación')),
                ('capacidad', models.CharField(blank=True, max_length=70, verbose_name='Capacidad de Diseño/Operativa')),
                ('potencia', models.CharField(blank=True, max_length=20, verbose_name='Potencia')),
                ('presion', models.CharField(blank=True, max_length=20, verbose_name='Presión descarga')),
                ('producto', models.CharField(blank=True, max_length=20, verbose_name='Producto')),
                ('temperatura', models.CharField(blank=True, max_length=20, verbose_name='Temperatura')),
                ('voltaje', models.CharField(blank=True, max_length=20, verbose_name='Voltaje')),
                ('fases', models.CharField(blank=True, max_length=20, verbose_name='Nro. de Fases')),
                ('datasheet', models.FileField(blank=True, null=True, upload_to='', validators=[registro.models.validate_file_extension], verbose_name='Datasheet')),
                ('fu_mantenimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de último mantenimiento integral')),
                ('estado', models.CharField(choices=[('O', 'Operativo'), ('F', 'Fuera de Servicio')], default='O', max_length=9, verbose_name='Estado Operativo')),
                ('observaciones', models.CharField(blank=True, max_length=100, verbose_name='Observaciones')),
                ('ingresado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.planta')),
                ('planta_secundaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.plantasecundaria')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.sistema')),
                ('subsistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.subsistema')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='equipo_principal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='planta_secundaria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registro.plantasecundaria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipo',
            name='subsistema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registro.subsistema'),
            preserve_default=False,
        ),
    ]