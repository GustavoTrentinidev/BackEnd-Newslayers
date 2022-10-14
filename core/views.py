from core.models.Midia import Midia
from core.models.Midia_user import Midia_user
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Topico, Noticia, Comentario, Curtida, Midia
from core.serializers import UsuarioSerializer, TopicoSerializer, NoticiaSerializer, CriarNoticiaSerializer, ComentarSerializer,UsuarioPostSerializer, CurtirSerilializer, MIDIAUSERPOSTSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return UsuarioSerializer
        return UsuarioPostSerializer

class TopicoViewSet(ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

class NoticiaViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Noticia.objects.all()
        idtopico = self.request.query_params.get('idtopico') 
        #Para filtrar pelo id é necessário utilizar um url como: http://127.0.0.1:8000/noticias/?idtopico=3
        if idtopico is not None:
            queryset = queryset.filter(topico_idtopico=idtopico)
        return queryset 

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return NoticiaSerializer
        return CriarNoticiaSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarSerializer

class CurtidaViewSet(ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtirSerilializer

class MIDIAUSERViewSet(ModelViewSet):
    queryset = Midia_user.objects.all()
    serializer_class = MIDIAUSERPOSTSerializer