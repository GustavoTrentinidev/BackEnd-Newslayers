from django.contrib import admin
from django.urls import path, include

from core.views import UsuarioViewSet, TopicoViewSet, NoticiaViewSet, ComentarioViewSet, CurtidaViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'topicos', TopicoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'curtidas', CurtidaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
