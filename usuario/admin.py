from django.contrib import admin
from usuario.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'cpf')
    # fieldsets = (("informações pessoais"), {"fields": ("first_name", "last_name")}),