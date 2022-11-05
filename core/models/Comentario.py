from django.db import models
from datetime import datetime
from .Noticia import Noticia
from django.contrib.auth import get_user_model

date = str(datetime.now()).split(' ')[0]

class Comentario(models.Model):
    def __str__(self):
        return f'({self.noticia_idnoticia}) {self.user_iduser}: {self.textocomentario}'
    datacomentario = models.DateField(default=date)
    textocomentario = models.CharField(max_length=240)
    user_iduser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comentarios")
    noticia_idnoticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="comentarios")
