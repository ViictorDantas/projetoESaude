from rest_framework import routers
from usuario.viewsets import UsuarioViewSet

usuario_router = routers.DefaultRouter()
usuario_router.register('usuario', UsuarioViewSet)
