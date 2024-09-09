from django.contrib import admin
from paciente.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cpf', 'email')
    # fieldsets = (("informações pessoais"), {"fields": ("first_name", "last_name")}),
