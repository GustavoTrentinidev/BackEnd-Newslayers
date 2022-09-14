from .Noticia import Noticia
from django.db import models


class Midia(models.Model):
    midiapath = models.CharField(max_length=5000)
    noticia_idnoticia = models.ForeignKey(Noticia, on_delete=models.PROTECT, related_name="midia")
