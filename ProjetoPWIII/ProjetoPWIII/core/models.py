from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    cor = models.CharField(max_length=19, verbose_name='Cor do carro')
    valor = models.DecimalField(decimal_places=2 , max_digits=10, verbose_name='Valor')

    class Meta:
        verbose_name ='Carro'
        verbose_name_plural ='Carros'

        def __str_(self):
            return self.nome
