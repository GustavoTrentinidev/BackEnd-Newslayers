from .Noticia import Noticia
from django.db import models


class Midia(models.Model):
    midiapath = models.FileField(upload_to='media/')
    noticia_idnoticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="midia")
