# Generated by Django 2.0.2 on 2018-10-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20181017_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsista',
            name='projeto_atual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atuacao', to='core.ProjetoDenominacao'),
        ),
        migrations.AlterField(
            model_name='projetodenominacao',
            name='participante',
            field=models.ManyToManyField(blank=True, to='core.Bolsista'),
        ),
    ]