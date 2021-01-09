from django.db import models
from ocorrencia.models import Ocorrencia
from localrecebedor.models import (
    AgenteRecebedor,
    LocalRecebedor
)
from observacao.models import Observacao
from veiculo.models import Veiculo


class Calibre(models.Model):
    calibre = models.CharField(
              'Calibre', max_length=20,
              help_text='Informe o calibre')

    class Meta:
        verbose_name = 'Calibre'
        verbose_name_plural = 'Calibres'
        db_table = 'calibre'

    def __str__(self):
        return self.calibre


class AcessoriosOcorrencia(models.Model):
    ocorrencia = models.ForeignKey(
                 Ocorrencia,
                 verbose_name='Ocorrência',
                 on_delete=models.CASCADE,
                 related_name='acessoriosocorrencia_ocorrencia',
                 help_text='Informe a Ocorrência')

    class Meta:
        verbose_name = 'Apreensão da ocorrência'
        verbose_name_plural = 'Apreensões da ocorrência'
        db_table = 'acessoriosocorrencia'

    def __str__(self):
        return '{}'.format(self.ocorrencia)


class MunicaoAcessorio(models.Model):
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrencia',
                           on_delete=models.CASCADE,
                           related_name='municaoacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    municao = models.ForeignKey(
              Calibre, verbose_name='Calibre',
              on_delete=models.CASCADE,
              help_text='Informe o calibre')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor,
                      verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor,
                     verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a observação')

    quantidade = models.IntegerField(
                 'Quantidade', help_text='Informe a quantidade')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de munição'
        verbose_name_plural = 'Apreensão de munições'
        db_table = 'municaoacessorio'

    def __str__(self):
        return '{}'.format(self.municao)


class VeiculoAcessorio(models.Model):
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrência',
                           on_delete=models.CASCADE,
                           related_name='veiculoacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    veiculo = models.ForeignKey(
              Veiculo, verbose_name='Veículo',
              on_delete=models.CASCADE, help_text='Informe o veículo')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor,
                      verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor,
                     verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de veículo'
        verbose_name_plural = 'Apreensão de veículos'
        db_table = 'veiculoacessorio'

    def __str__(self):
        return '{}'.format(self.veiculo)


class TipoDoc(models.Model):
    tipo = models.CharField(
           'Tipo de documento', max_length=30,
           help_text='Informe qual o tipo de documento')

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documento'
        db_table = 'tipodoc'

    def __str__(self):
        return '{}'.format(self.tipo)


class DocAcessorio(models.Model):
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrência',
                           on_delete=models.CASCADE,
                           related_name='docacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    tipodoc = models.ForeignKey(
              TipoDoc, verbose_name='Tipo de documento',
              on_delete=models.CASCADE,
              help_text='Informe o tipo de Documento')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor, verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor, verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    numero = models.CharField(
             'Número', max_length=50, blank=True,
             null=True, help_text='Informe o Número')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de Atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de documento'
        verbose_name_plural = 'Apreensão de documentos'
        db_table = 'docacessorio'

    def __str__(self):
        return '{}'.format(self.tipodoc)


class TiposDiversos(models.Model):
    tipo = models.CharField(
           'Tipo de objeto', max_length=30,
           help_text='Informe qual o tipo de objeto')

    class Meta:
        verbose_name = 'Tipo de objeto'
        verbose_name_plural = 'Tipos de objeto'
        db_table = 'tipodiversos'

    def __str__(self):
        return self.tipo


class DiversosAcessorio(models.Model):
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrência',
                           on_delete=models.CASCADE,
                           related_name='diversosacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    tipodiversos = models.ForeignKey(
                   TiposDiversos, verbose_name='Objeto',
                   on_delete=models.CASCADE,
                   help_text='Informe o tipo')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor, verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor, verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    descricao = models.TextField(
                'Descrição', help_text='Informe uma Descrição')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de Atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de objeto'
        verbose_name_plural = 'Apreensão de objetos'
        db_table = 'diversosacessorio'

    def __str__(self):
        return '{}'.format(self.tipodiversos)


class FabricanteArma(models.Model):
    fabricantearma = models.CharField(
                     'Fabricante da arma', max_length=255,
                     help_text='Informe o Fabricante')
    sigla = models.CharField(
            'Sigla do fabricante', max_length=20,
            help_text='Informe a Sigla do fabricante')

    class Meta:
        verbose_name = 'Fabricante da arma'
        verbose_name_plural = 'Fabricantes de arma'
        db_table = 'fabricantearma'

    def __str__(self):
        return self.sigla


class TipoArma(models.Model):
    tipo = models.CharField(
           'Tipo de arma', max_length=50,
           help_text='Informe o tipo de arma')

    class Meta:
        verbose_name = 'Tipo de arma'
        verbose_name_plural = 'Tipos de arma'
        db_table = 'tipoarma'

    def __str__(self):
        return self.tipo


class Arma(models.Model):
    tipoarma = models.ForeignKey(
               TipoArma, verbose_name='Tipo de arma',
               on_delete=models.CASCADE,
               help_text='Informe o tipo de arma')
    fabricantearma = models.ForeignKey(
                     FabricanteArma, verbose_name='Fabricante da arma',
                     on_delete=models.CASCADE, null=True, blank=True,
                     help_text='Informe o fabricante')
    calibre = models.ForeignKey(
              Calibre, verbose_name='Calibre',
              on_delete=models.CASCADE, null=True,
              blank=True, help_text='Informe o calibre')

    modelo = models.CharField(
             'Modelo', max_length=20,
             help_text='Informe o modelo')
    numeroserie = models.CharField(
                  'Número de série', max_length=30,
                  null=True, blank=True,
                  help_text='Informe o número de série')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de Atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'
        db_table = 'arma'

    def __str__(self):
        return self.modelo


class ArmaAcessorio(models.Model):
    arma = models.ForeignKey(
           Arma, verbose_name='Arma',
           on_delete=models.CASCADE, help_text='Informe a arma')
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrência',
                           on_delete=models.CASCADE,
                           related_name='armaacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor, verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor, verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField('Data de Atualização',
                                           auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de arma'
        verbose_name_plural = 'Apreensão de armas'
        db_table = 'armaacessorio'

    def __str__(self):
        return '{}'.format(self.arma)


class TipoDroga(models.Model):
    tipo = models.CharField(
           'Tipo de droga', max_length=20,
           help_text='Informe o tipo')

    class Meta:
        verbose_name = 'Tipo de droga'
        verbose_name_plural = 'Tipos de droga'
        db_table = 'tipodroga'

    def __str__(self):
        return '{}'.format(self.tipo)


class ArmazenamentoDroga(models.Model):
    armazenamento = models.CharField(
                    'Estado da droga', max_length=20,
                    help_text='Informe o estado da droga')

    class Meta:
        verbose_name = 'Estado da droga'
        verbose_name_plural = 'Estados de drogas'
        db_table = 'armazenamentodroga'

    def __str__(self):
        return '{}'.format(self.armazenamento)


class UnidadeMedida(models.Model):
    unidade = models.CharField(
              'Unidade de medida', max_length=5,
              help_text='Informe a unidade de medida')

    class Meta:
        verbose_name = 'Unidade de medida'
        verbose_name_plural = 'Unidades de medida'
        db_table = 'unidademedida'

    def __str__(self):
        return self.unidade


class DrogaAcessorio(models.Model):
    acessoriosocorrencia = models.ForeignKey(
                           AcessoriosOcorrencia,
                           verbose_name='Apreensão da Ocorrência',
                           on_delete=models.CASCADE,
                           related_name='drogaacessorio_acessoriosocorrencia',
                           help_text='Informe a apreensão da ocorrência')
    agenterecebedor = models.ForeignKey(
                      AgenteRecebedor, verbose_name='Agente Recebedor',
                      on_delete=models.CASCADE,
                      help_text='Informe o Agente recebedor')
    localrecebedor = models.ForeignKey(
                     LocalRecebedor, verbose_name='Local Recebedor',
                     on_delete=models.CASCADE,
                     help_text='Informe o Local recebedor')
    tipodroga = models.ForeignKey(
                TipoDroga, verbose_name='Droga',
                on_delete=models.CASCADE,
                help_text='Informe a droga')
    armazenamentodroga = models.ForeignKey(
                ArmazenamentoDroga, verbose_name='Estado da droga',
                on_delete=models.CASCADE,
                help_text='Informe o estado da droga')
    quantidade = models.IntegerField(
                 'Quantidade', help_text='Informe a Quantidade')
    medida = models.ForeignKey(
             UnidadeMedida, verbose_name='Unidade de medida',
             on_delete=models.CASCADE,
             help_text='Informe a unidade de medida')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a Observação')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Apreensão de droga'
        verbose_name_plural = 'Apreensão de drogas'
        db_table = 'drogaacessorio'

    def __str__(self):
        return '{} - {}{}'.format(self.tipodroga, self.quantidade, self.medida)
