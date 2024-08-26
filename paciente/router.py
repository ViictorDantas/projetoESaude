from rest_framework.routers import DefaultRouter
from paciente.viewsets import PacienteViewSet, ProntuarioViewSet


paciente_router = DefaultRouter()
paciente_router.register('paciente', PacienteViewSet)
paciente_router.register('prontuario', ProntuarioViewSet, basename='prontuario')