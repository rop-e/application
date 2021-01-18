from django.db import models
from policial.models import Policial
from endereco.models import Municipios
from observacao.models import Observacao

TIPO_VEICULO = (
    ('carro', 'CARRO'),
    ('moto', 'MOTO')
)


class TipoServico(models.Model):
    tiposervico = models.CharField(
                  'Tipo de Serviço', max_length=50,
                  help_text='Informe o tipo de serviço')

    class Meta:
        verbose_name = 'Tipo de serviço'
        verbose_name_plural = 'Tipos de serviço'
        db_table = 'tiposervico'

    def __str__(self):
        return self.tiposervico


class ModalidadedePoliciamento(models.Model):
    modalidade = models.CharField(
                 'Modalidade de Policiamento', max_length=50,
                 help_text='Informe a modalidade de policiamento')

    class Meta:
        verbose_name = 'Modalidade de policiamento'
        verbose_name_plural = 'Modalidades de policiamento'
        db_table = 'modalidadepoliciamento'

    def __str__(self):
        return self.modalidade


class Companhia(models.Model):
    companhia = models.CharField(
                'Companhia', max_length=50,
                help_text='Informe a companhia')
    comandante = models.ForeignKey(
                 'policial.Policial',
                 verbose_name='Comandante',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 related_name="comandante_companhia",
                 help_text='Informe o comandante da companhia')

    class Meta:
        verbose_name = 'Companhia'
        verbose_name_plural = 'Companhias'
        db_table = 'companhia'

    def __str__(self):
        return self.companhia


class Guarnicao(models.Model):
    tiposervico = models.ForeignKey(
                  TipoServico, verbose_name='Tipo de Serviço',
                  on_delete=models.CASCADE,
                  help_text='Informe o tipo de serviço')
    modalidadepoliciamento = models.ForeignKey(
                             ModalidadedePoliciamento,
                             verbose_name='Modalidade de policiamento',
                             on_delete=models.CASCADE,
                             help_text='Informe a modalidade de policiamento')
    companhia = models.ForeignKey(
                Companhia, verbose_name='Companhia',
                on_delete=models.CASCADE,
                help_text='Informe a Companhia')
    comandante = models.ForeignKey(
                 Policial, verbose_name='Comandante da guarnição',
                 on_delete=models.CASCADE,
                 help_text='Informe quem é o comandante')
    municipio = models.ForeignKey(
                Municipios, verbose_name='Município atuante',
                on_delete=models.CASCADE,
                help_text='Informe o município atuante')
    coordenadordearea = models.ForeignKey(
                        'policial.Policial',
                        verbose_name='Coordenador de área',
                        related_name='coordenadordearea',
                        on_delete=models.CASCADE,
                        help_text='Informe o coordenador de área')
    ativo = models.BooleanField(
            verbose_name='Está ativa?',
            default=True)
    
    bloqueadopor = models.ForeignKey(
                   'policial.Policial',
                   verbose_name='Bloqueado por',
                   related_name='guarnicao_bloqueadopor',
                   on_delete=models.CASCADE,
                   null=True, blank=True,
                   help_text='Bloqueado por')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 related_name='guarnicao_observacao',
                 blank=True, null=True,
                 help_text='Selecione a observação')

    relatorio = models.TextField(
                'Relatório de guarnição',
                null=True, blank=True)
    
    hash = models.TextField('Hash', blank=True)

    dataabertura = models.DateTimeField(
                   'Data de abertura', auto_now_add=True)
    datafechamento = models.DateTimeField(
                     'Data de fechamento',
                     blank=True, null=True)

    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Guarnição'
        verbose_name_plural = 'Guarnições'
        db_table = 'guarnicao'

    def __str__(self):
        return '{}'.format(self.comandante)


class GuarnicaoAIT(models.Model):
    guarnicao = models.ForeignKey(
                Guarnicao,
                verbose_name='Guarnição',
                on_delete=models.CASCADE,
                related_name='guarnicaoait_guarnicao',
                help_text='Informe a guarnição')

    codigo = models.CharField(
             'AIT extraído', max_length=20,
             help_text='Informe o código AIT extraído')
    tipoveiculo = models.CharField(
                  'Tipo de veículo', max_length=5, choices=TIPO_VEICULO,
                  help_text='Informe o tipo de veículo')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'AIT da guarnição'
        verbose_name_plural = 'AITs das guarnições'
        db_table = 'guarnicaoait'

    def __str__(self):
        return self.codigo


class GuarnicaoRRD(models.Model):
    guarnicao = models.ForeignKey(
                Guarnicao,
                verbose_name='Guarnição',
                on_delete=models.CASCADE,
                related_name='guarnicaorrd_guarnicao',
                help_text='Informe a guarnição')

    codigo = models.CharField(
             'RRD extraído', max_length=20,
             help_text='Informe o código RRD extraído')
    tipoveiculo = models.CharField(
                  'Tipo de veículo', max_length=5, choices=TIPO_VEICULO,
                  help_text='Informe o tipo de veículo')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'RRD da guarnição'
        verbose_name_plural = 'RRDs das guarnições'
        db_table = 'guarnicaorrd'

    def __str__(self):
        return self.codigo


class GuarnicaoTRAV(models.Model):
    guarnicao = models.ForeignKey(
                Guarnicao,
                verbose_name='Guarnição',
                on_delete=models.CASCADE,
                related_name='guarnicaotrav_guarnicao',
                help_text='Informe a guarnição')

    codigo = models.CharField(
            'TRAV extraído', max_length=20,
             help_text='Informe o código TRAV extraído')
    tipoveiculo = models.CharField(
                  'Tipo de veículo', max_length=5, choices=TIPO_VEICULO,
                  help_text='Informe o tipo de veículo')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'TRAV da guarnição'
        verbose_name_plural = 'TRAVs das guarnições'
        db_table = 'guarnicaotrav'

    def __str__(self):
        return self.codigo


class Permuta(models.Model):
    policial = models.ForeignKey(
               Policial, verbose_name='Policial permutado',
               on_delete=models.CASCADE,
               help_text='Informe quem é o policial')
    guarnicao_ultima = models.ForeignKey(
                       Guarnicao,
                       verbose_name='Última guarnição',
                       related_name='permuta_guarnicaoultima',
                       on_delete=models.CASCADE,
                       help_text='Informe a última guarnição')
    guarnicao_nova = models.ForeignKey(
                     Guarnicao,
                     verbose_name='Nova guarnição',
                     related_name='permuta_guarnicaonova',
                     null=True, blank=True,
                     on_delete=models.SET_NULL, #tem que deixar nulo se ele excluir a guarnição
                     help_text='Informe a nova guarnição')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Permuta'
        verbose_name_plural = 'Permutas'
        db_table = 'permuta'

    def __str__(self):
        return "{} - de {} para {}".format(self.policial, self.guarnicao_ultima, self.guarnicao_nova)
