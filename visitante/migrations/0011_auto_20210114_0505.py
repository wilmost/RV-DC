# Generated by Django 3.1.4 on 2021-01-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0010_auto_20210114_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituciones',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]
