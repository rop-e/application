from django.db import models
from localrecebedor.models import (
    AgenteRecebedor,
    LocalRecebedor
)
from observacao.models import Observacao
from guarnicao.models import Guarnicao
from endereco.models import Endereco
from veiculo.models import Veiculo


class TipoAcidente(models.Model):
    tipo = models.CharField(
           'Tipo de Acidente',
           max_length=100,
           help_text='Informe o tipo de acidente')

    class Meta:
        verbose_name = 'Tipo de acidente'
        verbose_name_plural = 'Tipos de acidente'
        db_table = 'tipoacidente'

    def __str__(self):
        return self.tipo


class CondicaoVia(models.Model):
    condicao = models.CharField(
               'Condição da Via',
               max_length=100,
               help_text='Informe a condição da via')

    class Meta:
        verbose_name = 'Condição da via'
        verbose_name_plural = 'Condições da via'
        db_table = 'condicaovia'

    def __str__(self):
        return self.condicao


class CondicaoSinalizacao(models.Model):
    condicao = models.CharField(
               'Condição da sinalização',
               max_length=100,
               help_text='Informe a condição da sinalização')

    class Meta:
        verbose_name = 'Condição da sinalização'
        verbose_name_plural = 'Condições de sinalização'
        db_table = 'condicaosinalizacao'

    def __str__(self):
        return self.condicao


class TracadoVia(models.Model):
    tracado = models.CharField(
               'Traçado da Via',
               max_length=100,
               help_text='Informe o traçado da via')

    class Meta:
        verbose_name = 'Traçado de via'
        verbose_name_plural = 'Traçados de via'
        db_table = 'tracadovia'

    def __str__(self):
        return self.tracado


class CondicaoMeteorologica(models.Model):
    condicao = models.CharField(
               'Condição Meteorológica',
               max_length=100,
               help_text='Informe a condição meteorológica')

    class Meta:
        verbose_name = 'Condição meteorológica'
        verbose_name_plural = 'Condições meteorológicas'
        db_table = 'condicaometeorologica'

    def __str__(self):
        return self.condicao


class Pavimentacao(models.Model):
    pavimentacao = models.CharField(
                   'Informe o tipo da pavimentação',
                   max_length=100,
                   help_text='Informe o tipo da pavimentação')

    class Meta:
        verbose_name = 'Pavimentação'
        verbose_name_plural = 'Pavimentações'
        db_table = 'pavimentacao'

    def __str__(self):
        return self.pavimentacao


class RAT(models.Model):
    guarnicao = models.ForeignKey(
                Guarnicao,
                verbose_name='Guarnição',
                on_delete=models.CASCADE,
                help_text='Informe a guarnição')
    endereco = models.ForeignKey(
               Endereco,
               verbose_name='Endereço',
               on_delete=models.CASCADE,
               help_text='Informe o endereço')
    tipoacidente = models.ForeignKey(
                   TipoAcidente,
                   verbose_name='Tipo de acidente',
                   on_delete=models.CASCADE,
                   help_text='Informe o tipo de acidente')
    condicaosinalizacao = models.ForeignKey(
                          CondicaoSinalizacao,
                          verbose_name='Condição da sinalização',
                          on_delete=models.CASCADE,
                          help_text='Informe a condição da sinalização')
    condicaovia = models.ForeignKey(
                  CondicaoVia,
                  verbose_name='Condição da via',
                  on_delete=models.CASCADE,
                  help_text='Informe a condição da via')
    condicaometeorologica = models.ForeignKey(
                            CondicaoMeteorologica,
                            verbose_name='Condição meteorológica',
                            on_delete=models.CASCADE,
                            help_text='Informe a condição meteorológica')
    pavimentacao = models.ForeignKey(
                   Pavimentacao,
                   verbose_name='Tipo de pavimentação',
                   on_delete=models.CASCADE,
                   help_text='Informe o tipo de pavimentação')
    tracadovia = models.ForeignKey(
                 TracadoVia,
                 verbose_name='Traçado da via',
                 on_delete=models.CASCADE,
                 help_text='Informe o traçado da via')

    status_previa = models.BooleanField(
                    verbose_name='Status de pré-visualização',
                    default=True)

    hash = models.TextField('Hash', blank=True)

    infracao = models.BooleanField(
               'Houve infração?',
               help_text='Informe se houve infração')
    relatorio = models.TextField(
                'Relatório da ocorrência',
                null=True, blank=True)

    dataocorrencia = models.DateTimeField('Data da ocorrência')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Registro de Acidente de Trânsito'
        verbose_name_plural = 'Registros de Acidente de Trânsito'
        db_table = 'rat'

    def __str__(self):
        return "{} - {} - ({})".format(self.tipoacidente, self.endereco, self.dataocorrencia.strftime("%d/%m/%Y"))


class RATObjetos(models.Model):
    rat = models.ForeignKey(
          RAT, verbose_name='Registro de Acidente de Trânsito',
          on_delete=models.CASCADE,
          related_name='ratobjetos_rat',
          help_text='Informe o Registro de Acidente de Trânsito')

    descricao = models.TextField(
                'Descrição', help_text='Informe uma descrição')
    quantidade = models.IntegerField(
                 'Quantidade', help_text='Informe a quantidade')
    localconducao = models.CharField(
                    'Local de condução',
                    max_length=100,
                    help_text='Informe o local de condução')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Objeto de RAT'
        verbose_name_plural = 'Objetos de RAT'
        db_table = 'ratobjetos'

    def __str__(self):
        return self.descricao


class RATVeiculos(models.Model):
    rat = models.ForeignKey(
          RAT, verbose_name='Registro de Acidente de Trânsito',
          on_delete=models.CASCADE,
          related_name='ratveiculos_rat',
          help_text='Informe o Registro de Acidente de Trânsito')
    veiculo = models.ForeignKey(
              Veiculo, verbose_name='Veículo',
              on_delete=models.CASCADE,
              help_text='Informe o veículo')
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
                 help_text='Informe a observação')

    condutor = models.BooleanField(
               'Condutor presente?',
               help_text='Informe se o condutor está presente')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Veículo de RAT'
        verbose_name_plural = 'Veículos de RAT'
        db_table = 'ratveiculos'

    def __str__(self):
        return "{}".format(self.veiculo)


class RATVeiculoEnvolvidos(models.Model):
    ratveiculos = models.ForeignKey(
                  RATVeiculos, verbose_name='Veículo',
                  on_delete=models.CASCADE,
                  help_text='Informe o veículo')
    envolvido = models.ForeignKey(
                'envolvido.Envolvido', verbose_name='Envolvido',
                on_delete=models.CASCADE,
                help_text='Informe o envolvido')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Envolvido em veículo de RAT'
        verbose_name_plural = 'Envolvidos em veículo de RAT'
        db_table = 'ratveiculoenvolvidos'

    def __str__(self):
        return '{} - {}'.format(self.ratveiculos, self.envolvido)
