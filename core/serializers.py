from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, HiddenField, CurrentUserDefault
from core.models import Usuario, Topico, Curtida, Midia_user, Noticia, Midia, Comentario


class CurtirSerilializer(ModelSerializer):
    iduser = HiddenField(default=CurrentUserDefault()) 
    class Meta:
        model = Curtida
        fields = "__all__"

class ComentarSerializer(ModelSerializer):
    user_iduser = HiddenField(default=CurrentUserDefault()) 
    class Meta:
        model = Comentario
        fields = "__all__"

class CurtidaNoticiaSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = ("iduser",)

class CurtidaUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Curtida
        fields = ("idnoticia",)

class MidiaUserSerializer(ModelSerializer):
    class Meta:
        model = Midia_user
        fields = ("midiabannerpath", "midiaprofilepath")

class MidiaNoticiaSerializer(ModelSerializer):
    class Meta: 
        model = Midia
        fields = ("midiapath",)

class UsuarioNoticiasSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    class Meta:
        model = Noticia
        fields = ("midia","noticiatitulo","texto","noticiadatacadastro")

class UsuarioSerializer(ModelSerializer):
    midia = MidiaUserSerializer()
    curtidas = CurtidaUsuarioSerializer(many=True)
    noticias = UsuarioNoticiasSerializer(many=True)
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

class UsuarioNaNoticia(ModelSerializer):
    midia = MidiaUserSerializer()
    class Meta:
        model = Usuario
        fields = ("username", "id" , "midia")

class ComentarioNoticiaSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id","datacomentario","textocomentario", "user_iduser")

class NoticiaSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)

    user_iduser = UsuarioNaNoticia()
    
    topico_idtopico = TopicoSerializer()
    comentarios = ComentarioNoticiaSerializer(many=True)
    curtidas = CurtidaNoticiaSerializer(many=True)
    class Meta:
        model = Noticia
        fields = "__all__"
    
    
    
class CriarNoticiaSerializer(ModelSerializer):
    midia = MidiaNoticiaSerializer(many=True)
    user_iduser = HiddenField(default=CurrentUserDefault()) 
    class Meta:
        model = Noticia
        fields = (
            "user_iduser",
            "topico_idtopico",
            "midia",
            "noticiatitulo",
            "texto"
        )
    def create(self, validated_data):
        fotos = validated_data.pop("midia")
        noticia = Noticia.objects.create(**validated_data)
        for foto in fotos:
            Midia.objects.create(**foto, noticia_idnoticia=noticia)
        return noticia
    