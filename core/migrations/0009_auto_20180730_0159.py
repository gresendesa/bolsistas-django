# Generated by Django 2.0.2 on 2018-07-30 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180730_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsista',
            name='projeto_atual',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='atuacao', to='core.ProjetoDenominacao'),
        ),
    ]
