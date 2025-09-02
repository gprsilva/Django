
from django.shortcuts import render, get_object_or_404,redirect
from .models import Especialidade, Medico
from .forms import AddEspecialidade, AddMedico

def mostrarMedico(request):
    medico_list = Medico.objects.all()
    return render(request, 'medico.html',{'medicos': medico_list})

def mostrarEspecialidade(request):
    esp_list = Especialidade.objects.all()
    return render(request, 'especialidade.html',{'especialidades': esp_list})

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
            
def editarE(request, especialidade_id):
    especialidade = get_object_or_404(Especialidade, id=especialidade_id) # tenta buscar o usuário pelo ID (id=contact_id), se não encontrar esse usuário, retorna na tela o erro 404.

    if request.method == 'POST':

        # popula o form com POST + instância existente
        especialidade.nome = request.POST.get('name')
        especialidade.descricao = request.POST.get('descricao')
        especialidade.save()

        # após salvar, redireciona ou renderiza a lista
        especialidade_list = Especialidade.objects.all()

        return redirect("especialidade")

    else:
        # se for GET, renderiza o template de edição passando o contact
        return render(request, 'editarE.html', {'especialidade': especialidade})
    
def excluirE(request, especialidade_id):
    especialidade = get_object_or_404(Especialidade, id=especialidade_id)
    especialidade.delete()
    return redirect("tela-esp")
                 
    
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