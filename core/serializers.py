from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Usuario, Topico, Curtida, Midia_user, Noticia, Midia, Comentario


class MidiaUserSerializer(ModelSerializer):
    class Meta:
        model = Midia_user
        fields = ("midiabannerpath", "midiaprofilepath")

class MidiaNoticiaSerializer(ModelSerializer):
    class Meta: 
        model = Midia
        fields = ("midiapath",)

class UsuarioSerializer(ModelSerializer):
    midia = MidiaUserSerializer()

    class Meta: 
        model = Usuario
        fields = "__all__"

    seguidores = SerializerMethodField()
    def get_seguidores(self,instance):
        nomes_seguidores = []
        seguidores = instance.seguidores.get_queryset()
        for seguidor in seguidores:
            nomes_seguidores.append({"id": seguidor.id, "username": seguidor.username})
        return nomes_seguidores
    
    seguindo = SerializerMethodField()
    def get_seguindo(self,instance):
        nomes_seguidos = []
        seguindo = instance.seguindo.get_queryset()
        for seguidos in seguindo:
            nomes_seguidos.append({"id":seguidos.id ,"username": seguidos.username})
        return nomes_seguidos

    def create(self, validated_data):
        fotos = validated_data.pop("midia")
        usuario  = Usuario.objects.create(**validated_data)
        Midia_user.objects.create(**fotos, user_iduser=usuario)
        return usuario

class TopicoSerializer(ModelSerializer):
    class Meta:
        model = Topico
        fields = "__all__"

class CurtidaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = "__all__"

class UsuarioNaNoticia(ModelSerializer):
    midia = MidiaUserSerializer()
    class Meta:
        model = Usuario
        fields = ("username", "id" , "midia")

class ComentarioSerializer(ModelSerializer):
    user_iduser = UsuarioNaNoticia()
    class Meta:
        model = Comentario
        fields = ("datacomentario","textocomentario", "user_iduser")

class NoticiaSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    user_iduser = UsuarioNaNoticia()
    topico_idtopico = TopicoSerializer()
    comentarios = ComentarioSerializer(many=True)
    curtidas = CurtidaSerializer(many=True)
    class Meta:
        model = Noticia
        fields = "__all__"
    
    def create(self, validated_data):
        fotos = validated_data.pop("midia")
        noticia = Noticia.objects.create(**validated_data)
        for foto in fotos:
            Midia.objects.create(**foto, noticia_idnoticia=noticia)
        return noticia
    
    # def update(self,instance,validated_data):
    #     instance.comentarios = validated_data.get('comentarios', instance.comentarios)
    #     instance.curtidas = validated_data.get('curtidas',instance.curtidas)
    #     return instance