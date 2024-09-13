from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']