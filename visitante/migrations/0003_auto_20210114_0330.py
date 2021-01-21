# Generated by Django 3.1.4 on 2021-01-14 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0002_auto_20201217_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='entrada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitante',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='visitante',
            name='salida',
            field=models.BooleanField(default=False),
        ),
    ]
