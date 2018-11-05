from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django import forms

from .models import Cargo as CargoModel, Entidade as EntidadeModel, Funcao as FuncaoModel, Usuario as  UsuarioModel, Bolsista as BolsistaModel, Documento as DocumentoModel, EmprestimoEquipamento as EmprestimoEquipamentoModel, Projeto as ProjetoModel
from .forms import CargoForm, EntidadeForm, FuncaoForm, ResponsavelForm, UsuarioForm, BolsistaForm, DocumentoForm, ProjetoForm, EmprestimoEquipamentoForm
from django.views.generic import View

from django.http import HttpResponse

from .abstract_views import GenericView, FormView

class Cargo(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Funcao(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Entidade(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Responsavel(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Usuario(FormView):
    template_name = 'cadastro/crud-withmodal.html'

class Projeto(FormView):

    template_name = 'cadastro/projeto.html'

class ProjetoList(GenericView):
    
    model = ProjetoModel
    template_name = 'cadastro/crud-projeto.html'


class Bolsista(FormView):

    template_name = 'cadastro/bolsista.html'

    def template_keys(self, **kwargs):

        pk = kwargs.get('pk', None)

        documento_form = DocumentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else DocumentoForm()
        documento_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        emprestimo_form = EmprestimoEquipamentoForm(initial={'bolsista': BolsistaModel.objects.get(pk=pk)}) if pk else EmprestimoEquipamentoForm()
        emprestimo_form.fields['bolsista'].widget = forms.HiddenInput() if pk else documento_form.fields['bolsista'].widget

        return {
            **super().template_keys(**kwargs),
            'content_title': 'Cadastrar Bolsistas / Pequisadores',
            'formf': documento_form,
            'forme': emprestimo_form,
            'documents': DocumentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'emprestimos': EmprestimoEquipamentoModel.objects.filter(bolsista=BolsistaModel.objects.get(pk=pk) if pk else None),
            'projects': BolsistaModel.objects.get(pk=pk).projeto_atual if pk else None,
            'pk': pk
        }

class BolsistaList(GenericView):

    model = BolsistaModel
    template_name = 'cadastro/crud-bolsista.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Bolsistas',
            'data': self.model.objects.all(),
            'form': BolsistaForm()
        }


class BolsistaMedia(Bolsista):

    def post(self, request, **kwargs):
        bolsista = BolsistaModel.objects.get(pk=request.POST.get('bolsista', None))
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bolsista-editar', pk=bolsista.pk)
        else:
            #form = BolsistaForm(instance=BolsistaModel.objects.get(pk=bolsista.pk)) if bolsista.pk else BolsistaForm()
            return self.get(request=request, form=form)

class BolsistaDocumento(BolsistaMedia):

    model = DocumentoModel

class BolsistaEmprestimoEquipamento(BolsistaMedia):

    model = EmprestimoEquipamentoModel

class Documento(GenericView):

    template_name = 'cadastro/file-viewer.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Preview de arquivo',
            'document': DocumentoModel.objects.get(pk=kwargs.get('pk', None))
        }

class EmprestimoEquipamento(GenericView):

    template_name = 'cadastro/emprestimo-viewer.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Empréstimo de Equipamento',
            'emprestimo': EmprestimoEquipamentoModel.objects.get(pk=kwargs.get('pk', None))
        }

class ProjetoList(GenericView):

    model = ProjetoModel
    template_name = 'cadastro/crud-projeto.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Projetos',
            'data': self.model.objects.all(),
            'form': ProjetoForm()
        }


class Projeto(FormView):

    template_name = 'cadastro/projeto.html'

    def template_keys(self, **kwargs):
        return {
            **super().template_keys(**kwargs),
            'content_title': 'Manter Projeto',
            'pk': kwargs.get('pk', None)
        }