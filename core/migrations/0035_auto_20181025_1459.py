# Generated by Django 2.0.2 on 2018-10-25 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20181025_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoDetalhes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', models.CharField(default='', max_length=64, verbose_name='Titulo da meta')),
                ('descricao_meta', models.TextField(default='', max_length=1024, verbose_name='Descrição da meta')),
                ('atividade_vinvulada', models.TextField(default='', max_length=1024, verbose_name='Atividade vinculada')),
                ('meta_especifica', models.TextField(default='', max_length=1024, verbose_name='Meta Específica')),
                ('metodologia', models.TextField(default='', max_length=1024, verbose_name='Metodologia')),
                ('atividades_previstas', models.TextField(default='', max_length=1024, verbose_name='Atividades previstas')),
                ('gestao_transferencia_tecnologia', models.TextField(default='', max_length=1024, verbose_name='Gestão de Transferência de Tecnologia')),
                ('meta_geral', models.CharField(choices=[('1', 'Controle de Andamento do Projeto'), ('2', 'Definição e Operacionalização da Arquitetura de Integração e Interoperação'), ('2', 'Modelo de Arquitetura e Medidas de Segutança dos Sistemas de Informações'), ('4', 'Acompanhamento da Operalização dos Processos de Gorvernança e TI na DPU')], default='', max_length=1, verbose_name='Meta')),
                ('atividade_geral', models.CharField(choices=[('1', 'INSERIR'), ('2', 'INSERIR'), ('2', 'INSERIR'), ('4', 'INSERIR'), ('5', 'INSERIR')], default='', max_length=1, verbose_name='Atividade')),
                ('resumo', models.TextField(default='', max_length=1024, verbose_name='Resumo do projeto')),
                ('file', models.ImageField(upload_to=None, verbose_name='Anexos')),
                ('entidade_concedente', models.ManyToManyField(related_name='concedente', to='core.Entidade')),
                ('entidade_proponente', models.ManyToManyField(related_name='proponente', to='core.Entidade')),
                ('participante', models.ManyToManyField(to='core.Bolsista')),
                ('responsavel_concedente', models.ManyToManyField(related_name='concedente', to='core.Responsavel')),
                ('responsavel_proponente', models.ManyToManyField(related_name='proponente', to='core.Responsavel')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='atividade_geral',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='atividade_vinvulada',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='atividades_previstas',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='descricao_meta',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='entidade_concedente',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='entidade_proponente',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='file',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='gestao_transferencia_tecnologia',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='meta_especifica',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='meta_geral',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='metodologia',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='participante',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='responsavel_concedente',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='responsavel_proponente',
        ),
        migrations.RemoveField(
            model_name='projetodenominacao',
            name='resumo',
        ),
        migrations.AddField(
            model_name='projetodenominacao',
            name='projeto_detalhes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detalhes', to='core.ProjetoDetalhes'),
        ),
    ]