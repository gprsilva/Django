
from django.shortcuts import render
from .models import Especialidade, Medico
from .forms import AddEspecialidade, AddMedico

def addEspecialidade(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddEspecialidade(request.POST)
        if django_form.is_valid():
           
            
            new_member_nome = django_form.data.get("nome")
            new_member_descricao = django_form.data.get("descricao")
            
            Especialidade.objects.create(
                nome =  new_member_nome, 
                descricao = new_member_descricao,
                )
                 
    
def addMedico(request):
    if request.method == 'POST':
        
        django_form = AddMedico(request.POST)
        if django_form.is_valid():
           
            
            new_member_nome = django_form.data.get("nome")
            new_member_endereco = django_form.data.get("endereco")
            new_member_telefone = django_form.data.get("telefone")
            new_member_email = django_form.data.get("email")
            new_member_data_nasc = django_form.data.get("data_nasc")
            new_member_crm = django_form.data.get("crm")
            new_member_especialidade = django_form.data.get("especialidade")
            
            Medico.objects.create(
                nome =  new_member_nome,
                endereco = new_member_endereco,
                telefone = new_member_telefone,
                email = new_member_email,
                dataNasc = new_member_data_nasc,
                crm = new_member_crm,
                especialidade = new_member_especialidade
                )