# Generated by Django 2.0.2 on 2018-05-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180501_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimoequipamento',
            name='tipo_equipamento',
            field=models.CharField(choices=[('1', 'Computador'), ('2', 'Projetor'), ('2', 'Microcontrolador'), ('4', 'Equipamento de Rede'), ('5', 'Outro')], default='1', max_length=1, verbose_name='Tipo de Equipamento'),
        ),
    ]