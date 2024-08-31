from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=255, null=True)
    senha = models.CharField(max_length=255, null=True)



