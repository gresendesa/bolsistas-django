# Generated by Django 2.0.2 on 2018-05-01 22:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180501_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoEquipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_equipamento', models.CharField(choices=[('1', 'Fotografia')], default='1', max_length=1, verbose_name='Tipo de Equipamento')),
                ('no_equipamento', models.CharField(max_length=64, verbose_name='Nome do Equipamento')),
                ('descricao_equipamento', models.CharField(max_length=512, verbose_name='Descrição do Equipamento')),
                ('nu_serie', models.CharField(max_length=64, verbose_name='Número de Série')),
                ('nu_patrimonio', models.CharField(max_length=64, verbose_name='Número do Equipamento')),
                ('dt_emprestimo', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Momento do Registro')),
                ('foto', models.FileField(upload_to='')),
                ('bolsista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bolsista')),
            ],
        ),
    ]