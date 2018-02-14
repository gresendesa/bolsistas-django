from django import forms
from common.forms import BaseForm, BaseFormControl
from core.models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, Projeto
from django.conf import settings
from utils.models import get_fields

class UsuarioForm(BaseForm):
    preview = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']
    class Meta:
        model = Usuario
        fields = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']

class CargoForm(BaseForm):
    preview = [f.name for f in Cargo._meta.get_fields()]
    class Meta:
        model = Cargo
        fields = get_fields(model)

class FuncaoForm(BaseForm):
    preview = [f.name for f in Funcao._meta.get_fields()]
    class Meta:
        model = Funcao
        fields = get_fields(model)

class EntidadeForm(BaseForm):
    preview = ['no_entidade', 'ic_ativo', 'cnpj', 'nu_municipio']
    class Meta:
        model = Entidade
        fields = get_fields(model)

class ResponsavelForm(BaseForm):
    preview = [f.name for f in Responsavel._meta.get_fields()]
    class Meta:
        model = Responsavel
        fields = get_fields(model)

class BolsistaForm(BaseFormControl):

    preview = ['no_bolsista', 'email', 'cpf', 'celular', 'ic_ativo']
    class Meta:
        model = Bolsista
        fields = get_fields(model)

class DocumentoForm(BaseFormControl):
    preview = [f.name for f in Documento._meta.get_fields()]
    class Meta:
        model = Documento
        fields = ['bolsista', 'tipo_documento', 'no_documento', 'arquivo']

class ProjetoForm(BaseForm):
    preview = [f.name for f in Projeto._meta.get_fields()]
    fk_entidade_proponente = forms.ModelChoiceField(queryset=Entidade.objects.all())
    class Meta:
        model = Projeto
        fields = get_fields(model)