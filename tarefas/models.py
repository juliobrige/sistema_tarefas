from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=20, default='gray')

    def __str__(self):
        return self.nome

PRIORIDADES = [
    ('alta', '🔥 Alta'),
    ('media', '🟡 Média'),
    ('baixa', '🟢 Baixa'),
]

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    agendada_para = models.DateTimeField(null=True, blank=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    mudancas_data = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao

# Create your models here.
