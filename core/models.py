from django.db import models
from datetime import datetime

class Usuario(models.Model):
    def __str__(self):
        return self.nome
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    senha = models.CharField(max_length=45)
    tipousuario = models.IntegerField(default=0)


class Seguir(models.Model):
    def __str__(self):
        return (self.usuarioSeguidor.nome + ' seguindo ' + self.usuarioSeguido.nome)
    usuarioSeguido = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='seguindo')
    usuarioSeguidor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='seguidores')
    class Meta:
        verbose_name_plural = "Seguir"

class Topico(models.Model):
    def __str__(self):
        return self.nometopico
    nometopico = models.CharField(max_length=45)

class Noticia(models.Model):
    def __str__(self):
        return self.noticiatitulo
    noticiatitulo = models.CharField(max_length=180)
    texto = models.CharField(max_length=7000)
    noticiadatacadastro = models.DateField(default=datetime.now)
    user_iduser = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    topico_idtopico = models.ForeignKey(Topico, on_delete=models.PROTECT)

class Comentario():
    datacomentario = models.DateField(default=datetime.now)
    textocomentario = models.CharField(max_length=240)
    user_iduser = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    noticia_idnoticia = models.ForeignKey(Noticia, on_delete=models.PROTECT)
