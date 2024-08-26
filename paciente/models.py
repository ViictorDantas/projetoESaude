from django.db import models

class Paciente(models.Model):

    nome = models.CharField(null=False, blank=False, max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    email = models.EmailField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    numero_residencia = models.IntegerField()
    
class Prontuario(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    exames = models.FileField(upload_to='exames/', max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)