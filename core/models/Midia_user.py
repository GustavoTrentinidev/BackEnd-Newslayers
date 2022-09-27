from django.db import models
from django.contrib.auth import get_user_model


class Midia_user(models.Model):
    midiabannerpath = models.CharField(max_length=5000)
    midiaprofilepath = models.CharField(max_length=5000)
    user_iduser = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, related_name="midia")