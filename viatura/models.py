from django.db import models
from observacao.models import Observacao

STATUS_VIATURA = (
    ('operacional', 'OPERACIONAL'),
    ('manutencao', 'EM MANUTENÇÃO'),
    ('parado', 'PARADO')
)


class Viatura(models.Model):
    modelo = models.CharField(
             'Modelo', max_length=80,
             help_text='Informe o modelo')
    ano = models.IntegerField(
          'Ano', help_text='Informe o ano')
    numero_viatura = models.CharField(
                     'Identificação da viatura', max_length=10, unique=True,
                     help_text='Informe a identificação da viatura')
    status = models.CharField(
             'Status', max_length=15,
             choices=STATUS_VIATURA,
             help_text='Informe o status')
    placa = models.CharField(
            'Placa', max_length=10, help_text='Informe a placa')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Viatura'
        verbose_name_plural = 'Viaturas'
        db_table = 'viatura'

    def __str__(self):
        return self.numero_viatura
