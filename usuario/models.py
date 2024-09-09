from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    first_name = models.CharField(max_length=100)  # Sobrescreve o campo 'first_name' do AbstractUser
    last_name = models.CharField(max_length=100)   # Sobrescreve o campo 'last_name' do AbstractUser
    telefone = models.CharField(max_length=15)  # Exemplo de telefone com formato (xx) xxxxx-xxxx
    cpf = models.CharField(max_length=11, unique=True)  # CPF com 11 dígitos
    email = models.EmailField(max_length=100, unique=True)  # Já existe no AbstractUser, mas pode personalizar
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10) 
    cep = models.CharField(max_length=8)  # CEP no formato xxxxxxxx (sem hífen)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
