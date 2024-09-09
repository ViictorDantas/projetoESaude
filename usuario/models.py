from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Usuario(AbstractUser):
    generos =[
        ('M','Masculino'),
        ('F','Feminino'),
    ]

    telefone = models.CharField(max_length=15)  # formato (xx) xxxxx-xxxx
    cpf = models.CharField(max_length=11, unique=True)  # CPF com 11 dígitos
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices= generos)
    email = models.EmailField(max_length=255, unique=True)  # Já existe no AbstractUser
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    numero_residencia = models.CharField(max_length=10) 
    cep = models.CharField(max_length=8)  # formato xxxxxxxx (sem hífen)

    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  # Define um related_name único
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',  # Define um related_name único
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
