from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Especialidade(models.Model):
    especialidade = models.CharField(max_length=50)

class Plano_Saude(models.Model):
    plano = models.CharField(max_length=50)

class Sexo(models.Model):
    SEXO = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    ]

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=10, choices=Sexo.SEXO)
    data_nascimento = models.DateField()
    telefone = models.BigIntegerField()
    planos_aceitos = models.ForeignKey(Plano_Saude, on_delete=models.CASCADE)
    classificacao = models.FloatField(default=0)
    bio = models.CharField(max_length=300, null=True, blank=True)