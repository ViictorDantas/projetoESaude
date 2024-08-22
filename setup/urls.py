from django.contrib import admin
from django.urls import path , include
from consulta.router import consulta_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(consulta_router.urls)),
    
]
