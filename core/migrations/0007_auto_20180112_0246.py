# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-12 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180112_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsista',
            name='pis_nit',
            field=models.CharField(blank=True, max_length=32, verbose_name='PIS ou NIT'),
        ),
    ]
