from django.contrib import admin
from paciente.models import Paciente, Prontuario


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')


@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'exames', 'data_criacao')

