from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Topico, Curtida, Noticia
from core.serializers import UsuarioSerializer, TopicoSerializer, NoticiaSerializer, CriarEditarNoticiaSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TopicoViewSet(ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

class NoticiaViewSet(ModelViewSet):
    queryset = Noticia.objects.all()
    # serializer_class = NoticiaSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return NoticiaSerializer
        return CriarEditarNoticiaSerializer