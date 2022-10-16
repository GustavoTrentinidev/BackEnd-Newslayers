from django.db import models
from django.contrib.auth import get_user_model


class Midia_user(models.Model):
    midiabannerpath = models.FileField(upload_to='media/')
    midiaprofilepath = models.FileField(upload_to='media/')
    user_iduser = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="midia")