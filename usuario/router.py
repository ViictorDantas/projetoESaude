from rest_framework import routers
from usuario.viewsets import UsuarioViewSet

usuario_router = routers.DefautRouter()
usuario_router.reguister('usuario', UsuarioViewSet)
