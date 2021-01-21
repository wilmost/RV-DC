# Generated by Django 3.1.4 on 2021-01-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0004_auto_20210114_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('autorizador', models.CharField(max_length=100)),
                ('email_autorizador', models.EmailField(max_length=100)),
                ('Tel_autorizador', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='visitante',
            name='duracion',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]