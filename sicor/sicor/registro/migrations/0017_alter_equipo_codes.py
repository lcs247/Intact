# Generated by Django 4.0 on 2022-01-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0016_alter_equipo_fu_mantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='codes',
            field=models.CharField(editable=False, max_length=70),
        ),
    ]