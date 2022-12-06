from django.contrib import admin
from django.urls import path, include

from core.views import UsuarioViewSet, TopicoViewSet, NoticiaViewSet, ComentarioViewSet, CurtidaViewSet, MIDIAUSERViewSet, UsuarioLogado, TodasNoticiasView

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'topicos', TopicoViewSet)
router.register(r'noticias', NoticiaViewSet, basename="Noticias")
router.register(r'comentarios', ComentarioViewSet, basename="Comentarios")
router.register(r'curtidas', CurtidaViewSet)
router.register(r'midias-usuarios', MIDIAUSERViewSet)
router.register(r'detail', UsuarioLogado, basename="usuariologado")
router.register(r'noticias-all', TodasNoticiasView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
