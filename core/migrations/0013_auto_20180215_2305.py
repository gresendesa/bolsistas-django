# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-15 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_merge_20180214_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='fk_bolsista',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bolsista', to='core.Bolsista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='fk_funcao',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='funcao', to='core.Funcao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='no_cargo',
            field=models.CharField(max_length=32, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='funcao',
            name='no_funcao',
            field=models.CharField(max_length=32, unique=True, verbose_name='Nome'),
        ),
    ]