from django.db import models
from policial.models import Policial
from viatura.models import Viatura
from guarnicao.models import Guarnicao
from observacao.models import Observacao


class Funcao(models.Model):
    funcao = models.CharField(
             'Função', max_length=50,
             help_text='Informe a Função')

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
        db_table = 'funcao'

    def __str__(self):
        return self.funcao


class PolicialViatura(models.Model):
    policial = models.ForeignKey(
               Policial, verbose_name='Policial',
               on_delete=models.CASCADE,
               help_text='Selecione o policial')
    viatura = models.ForeignKey(
              Viatura, verbose_name='Viatura',
              on_delete=models.CASCADE,
              blank=True, null=True,
              help_text='Selecione a viatura')
    guarnicao = models.ForeignKey(
                Guarnicao, verbose_name='Guarnição',
                on_delete=models.CASCADE,
                help_text='Selecione a guarnição')
    funcao = models.ForeignKey(
             Funcao, verbose_name='Função',
             on_delete=models.CASCADE,
             help_text='Selecione a função do policial')
    condicaoviatura = models.ForeignKey(
                      Observacao,
                      on_delete=models.CASCADE,
                      verbose_name='Observações das condições da viatura',
                      blank=True, null=True,
                      help_text='Informe a condição da viatura')
    ativo = models.BooleanField(
            verbose_name='Está ativo?',
            default=True)

    kmsaida = models.CharField(
              'Quilometragem de saída',
              max_length=10, blank=True,
              help_text='Informe a Quilometragem de saída')
    kmvolta = models.CharField(
              'Quilometragem de volta',
              max_length=10, blank=True,
              help_text='Informe a Quilometragem de volta')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Policial Viatura'
        verbose_name_plural = 'Policiais Viatura'
        db_table = 'policialviatura'

    def __str__(self):
        return '{} {}'.format(self.policial, self.funcao)
