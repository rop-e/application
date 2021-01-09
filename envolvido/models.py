from django.db import models
from ocorrencia.models import Ocorrencia
from localrecebedor.models import (
    LocalRecebedor,
    AgenteRecebedor
)
from pessoa.models import Pessoa
from rat.models import RAT
from observacao.models import Observacao


class TipoEnvolvimento(models.Model):
    tipo = models.CharField(
           'Tipo de envolvimento', max_length=20,
           help_text='Informe o tipo de envolvimento')
    rat = models.BooleanField(
          'Registro de Acidente de Trânsito',
          default=False, help_text='É RAT?')

    class Meta:
        verbose_name = 'Tipo de envolvimento'
        verbose_name_plural = 'Tipos de envolvimento'
        db_table = 'tipoenvolvimento'

    def __str__(self):
        return self.tipo


class Envolvido(models.Model):
    pessoa = models.ForeignKey(
             Pessoa, verbose_name='Pessoa',
             on_delete=models.CASCADE,
             null=True, blank=True,
             help_text='Informe a pessoa')
    ocorrencia = models.ForeignKey(
                 Ocorrencia, verbose_name='Ocorrência',
                 on_delete=models.CASCADE, null=True, blank=True,
                 related_name='envolvido_ocorrencia',
                 help_text='Informe a ocorrência')
    rat = models.ForeignKey(
          RAT, verbose_name='Registro de Acidente de Trânsito',
          on_delete=models.CASCADE, null=True, blank=True,
          related_name='envolvido_rat',
          help_text='Informe o Registro de Acidente de Trânsito')
    tipoenvolvimento = models.ForeignKey(
                       TipoEnvolvimento, verbose_name='Tipo de envolvimento',
                       on_delete=models.CASCADE,
                       help_text='Informe o tipo de envolvimento')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor, verbose_name='Local destinado',
                     on_delete=models.CASCADE, null=True, blank=True,
                     help_text='Selecione o local destinado')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor, verbose_name='Agente recebedor',
                      on_delete=models.CASCADE, null=True, blank=True,
                      help_text='Selecione o local destinado')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Envolvido'
        verbose_name_plural = 'Envolvidos'
        db_table = 'envolvido'

    def __str__(self):
        return '{}'.format(self.pessoa)


class TipoLesao(models.Model):
    tipo = models.CharField(
           'Tipo de lesão', max_length=50,
           help_text='Informe o tipo de lesão')

    class Meta:
        verbose_name = 'Tipo de lesão'
        verbose_name_plural = 'Tipos de lesão'
        db_table = 'tipolesao'

    def __str__(self):
        return self.tipo


class Lesao(models.Model):
    envolvido = models.ForeignKey(
                Envolvido, verbose_name='Envolvido',
                on_delete=models.CASCADE,
                help_text='Informe o envolvido')
    tipolesao = models.ForeignKey(
                TipoLesao, verbose_name='Tipo de lesão',
                on_delete=models.CASCADE,
                help_text='Informe o tipo de lesão')

    descricao = models.CharField(
                'Descrição da lesão',
                max_length=255, help_text='Descreva a lesão')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Lesão'
        verbose_name_plural = 'Lesões'
        db_table = 'lesao'

    def __str__(self):
        return self.descricao
