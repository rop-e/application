from django.db import models
from policial.models import Policial
from guarnicao.models import Guarnicao
from observacao.models import Observacao

STATUS_RELATORIO = (
    ("pendente", "PENDENTE"),
    ("andamento", "EM ANDAMENTO"),
    ("finalizada", "FINALIZADA")
)

DESIGNADO_PARA = (
    ("coordenadordearea", "COORDENADOR DE ÁREA"),
    ("cicom", "CICOM"),
    ("comandantecia", "COMANDANTE DE CIA")
)


class OPOTipoEvento(models.Model):
    tipo = models.CharField(
           'Tipo de evento', max_length=50,
           help_text='Informe o tipo de evento')

    class Meta:
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipos de evento'
        db_table = 'opotipoevento'

    def __str__(self):
        return self.tipo


class OPO(models.Model):
    opotipoevento = models.ForeignKey(
                    OPOTipoEvento, verbose_name='Tipo de evento',
                    on_delete=models.CASCADE,
                    help_text='Informe o tipo de evento')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a observação')

    solicitantenome = models.CharField(
                      'Nome do solicitante', max_length=100,
                      help_text='Informe o nome do solicitante')
    solicitantecontato = models.CharField(
                         'Contato do solicitante', max_length=80,
                         null=True, blank=True,
                         help_text='Informe o contato do solicitante')
    titulo = models.CharField(
             'Título', max_length=100,
             help_text='Informe o título')
    datasolicitacao = models.DateTimeField('Data da solicitação')
    datainicio = models.DateTimeField('Data de início')
    datatermino = models.DateTimeField(
                  'Data de término', null=True, blank=True)
    numeroopo = models.CharField(
                'Número da OPO', max_length=50,
                unique=True,
                help_text='Informe o número da OPO')
    local = models.CharField(
            'Local da OPO', max_length=255,
            help_text='Informe o local da OPO')
    armamento = models.CharField(
                'Armamento', max_length=100,
                help_text='Informe o armamento')
    uniforme = models.CharField(
               'Uniforme', max_length=100,
               help_text='Informe o uniforme')
    designado = models.CharField(
                'Designado para', max_length=17,
                choices=DESIGNADO_PARA,
                help_text='Designe a OPO')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Ordem de Policiamento Ostensivo'
        verbose_name_plural = 'Ordens de Policiamento Ostensivo'
        db_table = 'opo'

    def __str__(self):
        return self.titulo


class OPORelatorio(models.Model):
    opo = models.ForeignKey(
          OPO, verbose_name='OPO',
          on_delete=models.CASCADE,
          help_text='Informe o OPO')
    guarnicao = models.ForeignKey(
                Guarnicao, verbose_name='Guarnição',
                on_delete=models.CASCADE,
                null=True, blank=True,
                help_text='Informe a guarnição')
    designador = models.ForeignKey(
                 'policial.Policial',
                 verbose_name='Designador',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe quem designou')

    local = models.CharField(
            'Local', max_length=255,
            null=True, blank=True,
            help_text='Informe o local')
    status = models.CharField(
             'Status', max_length=10,
             choices=STATUS_RELATORIO,
             help_text='Informe o status',
             default='pendente')
    relatorio = models.TextField('Relatório', null=True, blank=True)

    dataexecucao = models.DateTimeField('Data da execução')
    datafinalizacao = models.DateTimeField(
                      'Data de finalização', null=True, blank=True)

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        db_table = 'oporelatorio'

    def __str__(self):
        return '{} - {}'.format(self.opo, self.relatorio)


class OPOComandantesCIA(models.Model):
    opo = models.ForeignKey(
          OPO, verbose_name='OPO',
          on_delete=models.CASCADE,
          help_text='Informe o OPO')
    comandante = models.ForeignKey(
                 Policial,
                 verbose_name='Comandante de CIA',
                 on_delete=models.CASCADE,
                 help_text='Informe o comandante de CIA')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)
    
    class Meta:
        verbose_name = 'OPO comandante de CIA'
        verbose_name_plural = 'OPOs comandante de CIA'
        db_table = 'opocomandantescia'

    def __str__(self):
        return '{} - {}'.format(self.opo, self.comandante)
