# Generated by Django 4.0 on 2022-02-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0019_alter_equipo_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='codes',
            field=models.CharField(blank=True, default='????', max_length=70),
        ),
    ]