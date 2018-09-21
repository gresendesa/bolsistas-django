# Generated by Django 2.0.2 on 2018-09-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180921_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolsista',
            name='funcao',
            field=models.CharField(choices=[('1', '5'), ('2', '4'), ('2', '3'), ('4', '2'), ('5', '1')], default='1', max_length=1, verbose_name='Funcao'),
        ),
        migrations.AddField(
            model_name='projetobolsista',
            name='cat_bolsa',
            field=models.CharField(choices=[('1', 'Bolsa de aux. ao estudante'), ('2', 'Bolsa de aux. ao pesquisador ')], default='1', max_length=1, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='projetobolsista',
            name='funcao',
            field=models.CharField(choices=[('1', '5'), ('2', '4'), ('2', '3'), ('4', '2'), ('5', '1')], default='1', max_length=1, verbose_name='Funcao'),
        ),
        migrations.AddField(
            model_name='projetobolsista',
            name='mod_bolsa',
            field=models.CharField(choices=[('1', 'Mestrado'), ('2', 'Iniciação Científica'), ('3', 'Nível Médio'), ('4', 'Pesquisador Sênior'), ('5', 'Pesquisa Acadêmica'), ('6', 'Pesquisa, Desenvolvimento e Inovação PDI'), ('7', 'Apoio Operacional à Pesquisa')], default='1', max_length=1, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='bolsista',
            name='categoria',
            field=models.CharField(choices=[('1', 'Bolsa de aux. ao estudante'), ('2', 'Bolsa de aux. ao pesquisador ')], default='1', max_length=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='bolsista',
            name='modalidade',
            field=models.CharField(choices=[('1', 'Mestrado'), ('2', 'Iniciação Científica'), ('3', 'Nível Médio'), ('4', 'Pesquisador Sênior'), ('5', 'Pesquisa Acadêmica'), ('6', 'Pesquisa, Desenvolvimento e Inovação PDI'), ('7', 'Apoio Operacional à Pesquisa')], default='1', max_length=1, verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='bolsista',
            name='nivel',
            field=models.CharField(choices=[('1', '5'), ('2', '4'), ('2', '3'), ('4', '2'), ('5', '1')], default='1', max_length=1, verbose_name='Nivel'),
        ),
    ]
