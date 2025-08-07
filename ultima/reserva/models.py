from django.db import models

class Reserva(models.Model):
    nome_pet = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    dia_reserva = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return f"{self.nome_pet} - {self.dia_reserva}"
