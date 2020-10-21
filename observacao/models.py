from django.db import models


class Observacao(models.Model):
    observacao = models.TextField(
                 'Observação',
                 help_text='Informe a Observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Observação'
        verbose_name_plural = 'Observações'
        db_table = 'observacao'

    def __str__(self):
        return self.observacao
