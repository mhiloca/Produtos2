from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.nome
