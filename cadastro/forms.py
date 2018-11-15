from django import forms
from django.forms import ModelForm, Form
from .utils.lists import remove
from .models import Cargo, Entidade, Funcao, Responsavel, Usuario, Bolsista, Documento, EmprestimoEquipamento, Projeto, Participante, Meta, Atividade, Anexo, Emprego
from django.conf import settings
from .utils.models import get_fields, get_clean_fields
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.forms import UserChangeForm

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.preview = remove('id', self.preview)
        super(ModelForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        m = super(ModelForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m

class BaseFormControl(ModelForm):
    def __init__(self, *args, **kwargs):
        self.preview = remove('id', self.preview)
        super(ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class UsuarioForm(BaseForm):
    preview = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']
    class Meta:
        model = Usuario
        fields = ['email', 'no_completo', 'ic_ativo', 'ic_bolsista']

class CargoForm(BaseForm):
    preview = get_clean_fields(Cargo)
    class Meta:
        model = Cargo
        fields = get_fields(model)

class FuncaoForm(BaseForm):
    preview = ['no_funcao','ic_ativo']
    class Meta:
        model = Funcao
        fields = get_fields(model)

class EntidadeForm(BaseForm):
    preview = ['no_entidade', 'ic_ativo', 'cnpj', 'nu_municipio']
    class Meta:
        model = Entidade
        fields = get_fields(model)

class ResponsavelForm(BaseForm):
    preview = ['no_responsavel', 'ic_ativo', 'co_matricula']
    class Meta:
        model = Responsavel
        fields = get_fields(model)

class BolsistaForm(BaseFormControl):

    preview = ['no_bolsista', 'email', 'cpf', 'celular', 'ic_ativo']

    def is_valid(self):

        #parent built-in is_valid() method
        valid = super(BolsistaForm, self).is_valid()

        if self.cleaned_data['tipo_conta'] == '1' and self.cleaned_data['banco'] != '104':
            self._errors['poupanca_sem_caixa'] = '{} disponível somente para o banco {}'.format(dict(Bolsista.TIPO_CONTA).get('1'), dict(Bolsista.COD_BANCO).get('104'))
            return False

        return valid

    class Meta:
        model = Bolsista
        fields = get_fields(model)

class DocumentoForm(BaseForm):
    preview = get_clean_fields(Documento)
    class Meta:
        model = Documento
        fields = ['bolsista', 'tipo_documento', 'no_documento', 'arquivo']

class EmprestimoEquipamentoForm(BaseForm):
    preview = get_clean_fields(EmprestimoEquipamento)
    class Meta:
        model = EmprestimoEquipamento
        fields = get_fields(model, ignore=['dt_emprestimo'])

class ProjetoForm(BaseFormControl):
    preview = ['nome', 'sigla']
    #file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    empty_m = 'Selecione uma opção'
    entidade_proponente = forms.ModelChoiceField(queryset=Entidade.objects.filter(ic_ativo=True), empty_label=empty_m)
    entidade_concedente = forms.ModelChoiceField(queryset=Entidade.objects.filter(ic_ativo=True), empty_label=empty_m)

    responsavel_proponente = forms.ModelChoiceField(queryset=Responsavel.objects.filter(ic_ativo=True), empty_label=empty_m)
    responsavel_concedente = forms.ModelChoiceField(queryset=Responsavel.objects.filter(ic_ativo=True), empty_label=empty_m)

    responsavel_tecnico_proponente = forms.ModelChoiceField(queryset=Responsavel.objects.filter(ic_ativo=True), empty_label=empty_m)
    responsavel_tecnico_concedente = forms.ModelChoiceField(queryset=Responsavel.objects.filter(ic_ativo=True), empty_label=empty_m)

    metodologia = forms.CharField(widget=forms.Textarea)
    gestao_transferencia_tecnologia = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Projeto
        fields = get_fields(model)

class ParticipanteForm(BaseFormControl):
    preview = ['bolsista', 'funcao', 'valor_mensal']

    empty_m = 'Selecione uma opção'
    
    funcao = forms.ModelChoiceField(queryset=Funcao.objects.filter(ic_ativo=True), empty_label=empty_m)
    class Meta:
        model = Participante
        fields = get_fields(model)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Este bolsista já é participante deste projeto"
            }
        }

class ParticipanteProjetoForm(ParticipanteForm):

    bolsista = forms.ModelChoiceField(queryset=Bolsista.objects.filter(ic_ativo=True), empty_label=ParticipanteForm.empty_m)
    projeto = forms.ModelChoiceField(queryset=Projeto.objects.all(), empty_label=ParticipanteForm.empty_m, widget=forms.HiddenInput())


class ParticipanteBolsistaForm(ParticipanteForm):

    bolsista = forms.ModelChoiceField(queryset=Bolsista.objects.all(), empty_label=ParticipanteForm.empty_m, widget=forms.HiddenInput())
    projeto = forms.ModelChoiceField(queryset=Projeto.objects.all(), empty_label=ParticipanteForm.empty_m)


class MetaForm(BaseFormControl):
    preview = ['titulo', 'ic_ativo']
    descricao = forms.CharField(widget=forms.Textarea)

    projeto = forms.ModelChoiceField(queryset=Projeto.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Meta
        fields = get_fields(model)

class AtividadeForm(BaseFormControl):

    preview = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'ic_ativo']
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    meta = forms.ModelChoiceField(queryset=Meta.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Atividade
        fields = get_fields(model, ignore=['bolsistas'])

class AnexoForm(BaseForm):
    preview = get_clean_fields(Anexo)

    projeto = forms.ModelChoiceField(queryset=Projeto.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Anexo
        fields = get_fields(model)

class AtividadeSelect(Form):
    def __init__(self, pkmeta, **kwargs):
        super().__init__(**kwargs)
        meta = Meta.objects.get(pk=pkmeta)
        self.fields['atividades'].queryset = Atividade.objects.filter(meta=meta, ic_ativo=True)

    atividades = forms.ModelChoiceField(queryset=Atividade.objects.all(), empty_label='Selecione uma atividade')


class AtividadeBolsistaSelect(ModelForm):
    def __init__(self, pkprojeto, **kwargs):
        super().__init__(**kwargs)
        projeto = Projeto.objects.get(pk=pkprojeto)
        self.fields['participantes'].queryset = Participante.objects.filter(projeto=projeto, ic_ativo=True)

    participantes = forms.ModelMultipleChoiceField(queryset=Participante.objects.filter(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Atividade
        fields = ['participantes']

class EmpregoForm(BaseForm):
    preview = ['nome', 'tipo']
    tipo = forms.ChoiceField(choices=Emprego.TIPOS, widget=forms.RadioSelect())
    class Meta:
        model = Emprego
        fields = get_fields(model)