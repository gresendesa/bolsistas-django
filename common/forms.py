from django import forms
from django.forms import ModelForm
from utils.lists import remove

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.preview = remove('id', self.preview)
        super(ModelForm, self).__init__(*args, **kwargs)

class BaseFormControl(ModelForm):
    def __init__(self, *args, **kwargs):
        self.preview = remove('id', self.preview)
        super(ModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'