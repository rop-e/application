from django.db import models
from guarnicao.models import Guarnicao
from observacao.models import Observacao
from endereco.models import Endereco
from colorfield.fields import ColorField


class TipoOcorrencia(models.Model):
    tipoocorrencia = models.CharField(
                     'Tipo de Ocorrência', max_length=50,
                     help_text='Informe o tipo de ocorrência')

    class Meta:
        verbose_name = 'Tipo de ocorrência'
        verbose_name_plural = 'Tipos de ocorrência'
        db_table = 'tipoocorrencia'

    def __str__(self):
        return self.tipoocorrencia


class Infracao(models.Model):
    tipo = models.CharField(
           'Tipo penal', max_length=50,
           help_text='Informe o tipo penal')
    cor = ColorField(default="#FF0000")

    class Meta:
        verbose_name = 'Tipo de infração'
        verbose_name_plural = 'Tipos de infração'
        db_table = 'infracao'

    def __str__(self):
        return self.tipo


class Orgao(models.Model):
    orgao = models.CharField(
            'Órgão', max_length=80,
            help_text='Informe o Órgão')

    class Meta:
        verbose_name = 'Órgão'
        verbose_name_plural = 'Órgãos'
        db_table = 'orgao'

    def __str__(self):
        return self.orgao


class Ocorrencia(models.Model):
    tipoocorrencia = models.ForeignKey(
                     TipoOcorrencia,
                     verbose_name='Tipo de Ocorrência',
                     on_delete=models.CASCADE,
                     help_text='Informe o tipo de ocorrência')
    orgao = models.ForeignKey(
            Orgao,
            verbose_name='Órgão',
            on_delete=models.CASCADE, null=True,
            help_text='Informe o Orgão')
    guarnicao = models.ForeignKey(
                Guarnicao,
                verbose_name='Guarnição',
                on_delete=models.CASCADE,
                help_text='Informe a Guarnição')
    infracao = models.ForeignKey(
               Infracao, verbose_name='Tipo Penal',
               on_delete=models.CASCADE, null=True,
               help_text='Informe o tipo penal')
    endereco = models.ForeignKey(
               Endereco, verbose_name='Endereço da Ocorrência',
               on_delete=models.CASCADE,
               help_text='Informe o endereço da ocorrência')
    vinculo = models.ForeignKey(
              'ocorrencia.Ocorrencia',
              verbose_name='É vinculo de ocorrência?',
              on_delete=models.CASCADE,
              null=True, blank=True,
              help_text='Informe a ocorrência')
    
    status_previa = models.BooleanField(
                    verbose_name='Status de pré-visualização',
                    default=True)

    hash = models.TextField('Hash', blank=True)

    relatorio = models.TextField(
                'Relatório da ocorrência',
                null=True, blank=True)

    dataocorrencia = models.DateTimeField('Data da ocorrência')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'
        db_table = 'ocorrencia'

    def __str__(self):
        return "{}".format(self.relatorio)


class ObservacaoOcorrencia(models.Model):
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 help_text='Informe a observação')
    ocorrencia = models.ForeignKey(
                 Ocorrencia, verbose_name='Ocorrência',
                 on_delete=models.CASCADE,
                 help_text='Informe a ocorrência')
    autor = models.ForeignKey(
            'policial.Policial',
            verbose_name='Autor',
            on_delete=models.CASCADE,
            help_text='Informe o autor')
    ativo = models.BooleanField(
            verbose_name='Está ativa?',
            default=True)

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Aditamento da ocorrência'
        verbose_name_plural = 'Aditamentos da ocorrência'
        db_table = 'observacaoocorrencia'

    def __str__(self):
        return '{}'.format(self.ocorrencia)


class GuarnicaoApoio(models.Model):
    ocorrencia = models.ForeignKey(
                 Ocorrencia, verbose_name='Ocorrência',
                 on_delete=models.CASCADE,
                 help_text='Informe a Ocorrência')
    guarnicao = models.ManyToManyField(
                Guarnicao, verbose_name='Guarnição',
                help_text='Informe a guarnição de apoio')

    class Meta:
        verbose_name = 'Guarnição de Apoio'
        verbose_name_plural = 'Guarnições de Apoio'
        db_table = 'guarnicaoapoio'

    def __str__(self):
        return '{}'.format(self.guarnicao)
