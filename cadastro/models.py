from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
from .validators import cpf, lattes_url


class Usuario(AbstractUser):
    no_completo = models.CharField('Nome completo', max_length=64, unique=True)
    ic_ativo = models.BooleanField('Ativo', default=True)
    ic_bolsista = models.BooleanField('Bolsista', default=True)
    email = models.EmailField('Email', unique=True)

    class Meta:
        verbose_name = "usuário"


class Entidade(models.Model):
    co_entidade = models.CharField('Código', max_length=32, unique=True)
    no_entidade = models.CharField('Nome', max_length=32, unique=True)
    sg_entidade = models.CharField('Sigla', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')
    cnpj = models.IntegerField('CNPJ', unique=True)
    telefone = models.IntegerField('Telefone')
    cep = models.IntegerField('CEP')
    nu_municipio = models.IntegerField('Número do municipio')
    co_esfera = models.CharField('Esfera', max_length=32)
    de_endereco = models.CharField('Endereço', max_length=128)

    def __str__(self):
        return "{} - {}".format(self.no_entidade, self.sg_entidade)


class Cargo(models.Model):
    no_cargo = models.CharField('Nome', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')


class Funcao(models.Model):
    no_funcao = models.CharField('Nome', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')

    class Meta:
        verbose_name_plural = "funções"
        verbose_name = "função"

    def __str__(self):
        return self.no_funcao


class Responsavel(models.Model):
    no_responsavel = models.CharField('Nome', max_length=32, unique=True)
    cpf = models.IntegerField('CPF')
    telefone = models.IntegerField('Telefone')
    co_matricula = models.CharField('Matrícula', max_length=32, unique=True)
    ic_ativo = models.BooleanField('Ativo')

    class Meta:
        verbose_name_plural = "responsáveis"
        verbose_name = "responsável"

    def __str__(self):
        return self.no_responsavel



class Bolsista(models.Model):
    TIPOS_VINCULOS = (
        ('1', 'Servidor Público - Professor'),
        ('2', 'Servidor Público ou Empregado Público'),
        ('3', 'Colaborador sem vínculo com o serviço')
    )

    TIPO_CONTA = (
        ('1', 'Conta-poupança'),
        ('2', 'Conta-corrente')
    )

    COD_BANCO = (
        ('001', '001 - BANCO DO BRASIL S/A'),
        ('002', '002 - BANCO CENTRAL DO BRASIL'),
        ('003', '003 - BANCO DA AMAZONIA S.A'),
        ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A'),
        ('070', '070 - BANCO DE BRASILIA S.A'),
        ('104', '104 - CAIXA ECONOMICA FEDERAL'),
        ('237', '237 - BANCO BRADESCO S.A'),
        ('275', '275 - BANCO REAL S.A'),
        ('341', '341 - BANCO ITAU S.A'),
        ('409', '409 - UNIBANCO - UNIAO DOS BANCOS BRASILEIROS'),
        ('422', '422 - BANCO SAFRA S.A'),
        ('477', '477 - CITIBANK N.A'),
        ('502', '502 - BANCO SANTANDER S.A')

    )

    UFS = (
        ('AC', 'AC - Acre'),
        ('AL', 'AL - Alagoas'),
        ('AP', 'AP - Amapá'),
        ('AM', 'AM - Amazonas'),
        ('BA', 'BA - Bahia'),
        ('CE', 'CE - Ceará'),
        ('DF', 'DF - Distrito Federal'),
        ('ES', 'ES - Espírito Santo'),
        ('GO', 'GO - Goiás'),
        ('MA', 'MA - Maranhão'),
        ('MT', 'MT - Mato Grosso'),
        ('MS', 'MS - Mato Grosso do Sul'),
        ('MG', 'MG - Minas Gerais'),
        ('PA', 'PA - Pará'),
        ('PB', 'PB - Paraíba'),
        ('PR', 'PR - Paraná'),
        ('PE', 'PE - Pernambuco'),
        ('PI', 'PI - Piauí'),
        ('RJ', 'RJ - Rio de Janeiro'),
        ('RN', 'RN - Rio Grande do Norte'),
        ('RS', 'RS - Rio Grande do Sul'),
        ('RO', 'RO - Rondônia'),
        ('RR', 'RR - Roraima'),
        ('SC', 'SC - Santa Catarina'),
        ('SP', 'SP - São Paulo'),
        ('SE', 'SE - Sergipe'),
        ('TO', 'TO - Tocantins')
    )

    tipo_vinculo = models.CharField('Tipo de Vínculo', max_length=1, choices=TIPOS_VINCULOS, default='3')

    no_bolsista = models.CharField('Nome', max_length=32)
    email = models.EmailField('Email', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True, validators=[cpf])
    dt_nascimento = models.CharField('Data de Nascimento', max_length=10)
    rg = models.CharField('RG', max_length=32)
    orgao_expedidor = models.CharField('Órgão Expedidor', max_length=32)
    telefone = models.CharField('Telefone', max_length=32, blank=True)
    celular = models.CharField('Celular', max_length=32, blank=True)
    matricula = models.CharField('Matrícula', max_length=32, unique=True, blank=True)
    ic_ativo = models.BooleanField('Ativo')

    pis_nit = models.CharField('PIS ou NIT', max_length=32, blank=True)
    link_lattes = models.CharField('Lattes', max_length=128, unique=True, validators=[lattes_url])

    endereco = models.CharField('Endereço', max_length=128)
    cidade = models.CharField('Cidade', max_length=32)
    cep = models.CharField('CEP', max_length=32)
    uf = models.CharField('UF', max_length=2, choices=UFS, default='DF')

    banco = models.CharField('Banco', max_length=128, choices=COD_BANCO, default='001')
    agencia = models.CharField('Agência', max_length=32)
    tipo_conta = models.CharField('Tipo de Conta', max_length=1, choices=TIPO_CONTA, default='2')
    conta = models.CharField('Conta', max_length=32)

    email_unb = models.EmailField('Email UnB', unique=True, blank=True)
    telefone_local = models.CharField('Telefone Local', max_length=32, blank=True)

    class Meta:
        verbose_name_plural = "Bolsistas"
        verbose_name = "Bolsista"

    def __str__(self):
        return self.no_bolsista


class Documento(models.Model):
    TIPOS = (
        ('1', 'Fotografia'),
        ('2', 'Declaração'),
        ('3', 'Documento pessoal'),
        ('4', 'Certificado'),
    )
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE)
    tipo_documento = models.CharField('Tipo de Documento', max_length=1, choices=TIPOS, default='3')
    no_documento = models.CharField('Descrição', max_length=512)
    dt_cadastro = models.DateTimeField('Momento do Upload', default=datetime.now, blank=True)
    arquivo = models.FileField()

    @property
    def filename(self):
        return self.arquivo.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return self.tipo_documento

class EmprestimoEquipamento(models.Model):
    TIPOS = (
        ('1', 'Computador'),
        ('2', 'Projetor'),
        ('2', 'Microcontrolador'),
        ('4', 'Equipamento de Rede'),
        ('5', 'Outro'),
    )
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE)
    tipo_equipamento = models.CharField('Tipo de Equipamento', max_length=1, choices=TIPOS, default='1')
    descricao_equipamento = models.CharField('Descrição do Equipamento', max_length=512)
    nu_serie = models.CharField('Número de Série', max_length=64)
    nu_patrimonio = models.CharField('Número de Patrimônio', max_length=64)
    dt_emprestimo = models.DateTimeField('Momento do Registro', default=datetime.now, blank=True)
    foto = models.FileField()

    @property
    def filename(self):
        return self.foto.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return dict(EmprestimoEquipamento.TIPOS).get(self.tipo_equipamento)

class Projeto(models.Model):
    nome = models.CharField('Nome do Projeto', max_length=32)
    sigla = models.CharField('Sigla', max_length=32, unique=True)
    
    entidade_concedente = models.ForeignKey('Entidade', on_delete=models.CASCADE, related_name='entidadeconcedente', null=True, blank=True)
    entidade_proponente = models.ForeignKey('Entidade', on_delete=models.CASCADE ,related_name='entidadeproponente', null=True, blank=True)

    responsavel_concedente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rconcedente', null=True, blank=True)
    responsavel_proponente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rproponente', null=True, blank=True)

    responsavel_tecnico_concedente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rtconcedente', null=True, blank=True)
    responsavel_tecnico_proponente = models.ForeignKey('Responsavel', on_delete=models.CASCADE, related_name='rtproponente', null=True, blank=True)

    metodologia = models.CharField('Metodologia', max_length=1024, blank=True)

    gestao_transferencia_tecnologia = models.CharField('Gestão de Projeto e Transferência de Tecnologia', max_length=1024, blank=True)

    class Meta:
        verbose_name_plural = "Projetos"
        verbose_name = "Projeto"
    def __str__(self):
        return "{} - {}".format(self.sigla, self.nome)


class Participante(models.Model):
    bolsista = models.ForeignKey('Bolsista', on_delete=models.CASCADE, verbose_name="Bolsista")
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, verbose_name="Projeto")
    funcao = models.ForeignKey('Funcao', on_delete=models.CASCADE, verbose_name="Função")
    ic_ativo = models.BooleanField('Ativo')

    CATEGORIA = (
        ('1', 'Bolsa de aux. ao estudante'),
        ('2', 'Bolsa de aux. ao pesquisador '),
    )

    MODALIDADE = (
        ('1', 'Mestrado'),
        ('2', 'Iniciação Científica'),
        ('3', 'Nível Médio'),
        ('4', 'Pesquisador Sênior'),
        ('5', 'Pesquisa Acadêmica'),
        ('6', 'Pesquisa, Desenvolvimento e Inovação PDI'),
        ('7', 'Apoio Operacional à Pesquisa'),

    )

    NIVEL = (
        ('1', 'A'),
        ('2', 'B'),
        ('2', 'C'),
        ('4', 'D')
    )

    categoria = models.CharField('Categoria', max_length=1, choices=CATEGORIA, default='1')
    modalidade = models.CharField('Modalidade', max_length=1, choices=MODALIDADE, default='1')
    nivel = models.CharField('Nível', max_length=1, choices=NIVEL, default='1')

    inicio_vigencia = models.CharField('Início da Vigência', max_length=100,blank=True)
    termino_vigencia = models.CharField('Término da Vigência', max_length=100, blank=True)
    periodo_total = models.IntegerField('Período Total', blank=True)
    horas_semanais = models.IntegerField('Horas semanais', blank=True)
    valor_mensal = models.DecimalField('Valor mensal', max_digits=10, decimal_places=2, blank=True)
    valor_total = models.DecimalField('Valor total', max_digits=10, decimal_places=2, blank=True)


    class Meta:
        unique_together = ('projeto', 'bolsista',)

    def __str__(self):
        return "{}".format(self.bolsista.no_bolsista)

class Meta(models.Model):
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, verbose_name="Projeto")
    titulo = models.CharField('Título', max_length=100, blank=True)
    descricao = models.CharField('Descrição', max_length=1024, blank=True)
    ic_ativo = models.BooleanField('Ativo')

    def __str__(self):
        return "{}".format(self.titulo)

class Atividade(models.Model):
    meta = models.ForeignKey('Meta', on_delete=models.CASCADE, verbose_name="Meta")
    titulo = models.CharField('Título', max_length=100, blank=True)
    descricao = models.CharField('Descrição', max_length=1024, blank=True)
    data_inicio = models.CharField('Data de Início', max_length=100,blank=True)
    data_fim = models.CharField('Data de Fim', max_length=100, blank=True)
    ic_ativo = models.BooleanField('Ativo')
    participantes = models.ManyToManyField(Participante)

    def __str__(self):
        return "{}".format(self.titulo)


class Anexo(models.Model):
    
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE)
    arquivo = models.FileField()

    @property
    def filename(self):
        return self.arquivo.name.replace(settings.MEDIA_URL, '')

    def __str__(self):
        return self.tipo_documento


