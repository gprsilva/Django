from django.db import models

# Create your models here.
class Especialidade(models.Model):
    id_especialidade = models.BigAutoField(primary_key=True),
    nome = models.CharField(max_length=200),
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Medico(models.Model):
    id_medico = models.BigAutoField(primary_key=True),
    nome = models.CharField(max_length=200),
    endereco = models.CharField(max_length=200),
    telefone = models.CharField(max_length=200),
    email = models.CharField(max_length=200),
    data_nascimento = models.DateField(),
    crm = models.CharField(max_length=13),
    id_especialidade = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.nome


