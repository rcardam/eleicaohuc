from django.db import models

# Create your models here.

class Votacao(models.Model):
  crm = models.CharField(max_length=8, null=True, blank=True)
  nome = models.CharField(max_length=100, null=True, blank=True)
  cpf = models.CharField(max_length=11, verbose_name='CPF')
  dtvoto = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  voto = models.CharField(max_length=2, null=True, blank=True)
  
  def __str__(self) -> str:
    return f'{self.crm} - {self.nome}'
  
  class Meta:
    verbose_name = 'Eleição'
    verbose_name_plural = 'Eleições'
    db_table = 'votacao'

    
    

  
  
