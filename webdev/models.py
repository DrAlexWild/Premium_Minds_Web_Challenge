from django.db import models

# Create your models here.
class Utilizador(models.Model):
    nome = models.CharField(max_length=200)

    project_manager = models.BooleanField(default=False)
    developer = models.BooleanField(default=False)
    architect = models.BooleanField(default=False)
    email = models.CharField(max_length=200)
    palavra_passe = models.CharField(max_length=200)
    telefone = models.CharField(default="+351 000000000", max_length=15)

    def __str__(self):
        return self.nome[:200]