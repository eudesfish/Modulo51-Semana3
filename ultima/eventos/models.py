from django.db import models

class Categoria(models.Model):

    nome =  models.CharField('nome', max_length=50)
    descricao = models.TextField('descricao', blank=True)