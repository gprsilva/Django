from django import forms
from .models import Especialidade, Medico

class AddEspecialidade(forms.Form):
    class Meta:
        model = Especialidade
        fields =('nome', 'descricao')

class AddMedico(forms.Form):
    class Meta:
        model = Medico
        fields = ('nome', 'endereco', 'telefone', 'email', 'data_nasc', 'crm', 'especialidade')