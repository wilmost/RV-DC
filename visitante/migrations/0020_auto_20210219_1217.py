# Generated by Django 3.1.4 on 2021-02-19 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0019_auto_20210214_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instituciones',
            options={'ordering': ['tipo']},
        ),
    ]