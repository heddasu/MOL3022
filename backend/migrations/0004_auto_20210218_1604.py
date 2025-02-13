# Generated by Django 3.1.2 on 2021-02-18 16:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210218_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfm',
            name='adenin',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name=models.FloatField()),
        ),
        migrations.AlterField(
            model_name='pfm',
            name='cytosine',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name=models.FloatField()),
        ),
        migrations.AlterField(
            model_name='pfm',
            name='guanine',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name=models.FloatField()),
        ),
        migrations.AlterField(
            model_name='pfm',
            name='thymine',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, verbose_name=models.FloatField()),
        ),
    ]
