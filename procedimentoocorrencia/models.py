from django.db import models
from ocorrencia.models import Ocorrencia
from observacao.models import Observacao
from rat.models import RAT


class Procedimento(models.Model):
    procedimento = models.CharField(
                   'Procedimento', max_length=50,
                   help_text='Informe o procedimento utilizado na ocorrencia')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta():
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'
        db_table = 'procedimento'

    def __str__(self):
        return self.procedimento


class ProcedimentoOcorrencia(models.Model):
    procedimento = models.ForeignKey(
                   Procedimento, verbose_name='Procedimento',
                   on_delete=models.CASCADE,
                   help_text='Informe o procedimento')
    ocorrencia = models.ForeignKey(
                 Ocorrencia, verbose_name='Ocorrência',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a ocorrência')
    rat = models.ForeignKey(
          RAT, verbose_name='Registro de Acidente de Trânsito',
          on_delete=models.CASCADE,
          null=True, blank=True,
          help_text='Informe o Registro de Acidente de Trânsito')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 help_text='Informe a observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta():
        verbose_name = 'Procedimento da ocorrência'
        verbose_name_plural = 'Procedimentos da ocorrência'
        db_table = 'procedimentoocorrencia'

    def __str__(self):
        return '{}'.format(self.procedimento)
