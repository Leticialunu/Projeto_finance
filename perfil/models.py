from django.db import models

# Create your models here.

class Categoria(models.Model):
    Categoria = models.CharField(max_length=50,null=False,blank=False, verbose_name='Categoria')
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0, verbose_name='Valor do planejamneto')
    
    def __str__(self):
        return self.categoria
    
class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CX', 'Caixa'),
    )
    
    tipo_choices = (
        ('pf', 'Pessoa Fisica'),
        ('pj', 'Pessoa Juridica'),
    )
    
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2,choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='Icone')
    
    def __str__(self):
        return self.apelido