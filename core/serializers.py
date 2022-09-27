from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Usuario, Topico, Curtida, Midia_user


class MidiaUserSerializer(ModelSerializer):
    class Meta:
        model = Midia_user
        fields = ("midiabannerpath", "midiaprofilepath")

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