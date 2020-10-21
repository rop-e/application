from django.db import models
from observacao.models import Observacao


class Estados(models.Model):
    codigo_uf = models.IntegerField(
                'Código UF', primary_key=True,
                help_text='Informe o código UF')
    uf = models.CharField(
         'UF', max_length=2,
         help_text='Informe a UF')
    nome = models.CharField(
           'Nome do Estado', max_length=100,
           help_text='Informe o nome do Estado')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estados'

    def __str__(self):
        return self.nome


class Municipios(models.Model):
    codigo_uf = models.ForeignKey(
                Estados, verbose_name='Código UF',
                on_delete=models.CASCADE,
                help_text='Informe o código UF')

    codigo_ibge = models.IntegerField(
                  'Código IBGE', primary_key=True,
                  help_text='Informe o código do IBGE')
    nome = models.CharField(
           'Nome da cidade', max_length=100,
           help_text='Informe o nome da cidade')
    latitude = models.FloatField(
               'Latitude', max_length=8,
               help_text='Informe a latitude')
    longitude = models.FloatField(
                'Longitude', max_length=8,
                help_text='Informe a longitude')
    capital = models.BooleanField(
              'É a capital?',
              help_text='Informe se este município é a capital')

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        db_table = 'municipios'

    def __str__(self):
        return '{} - {}'.format(self.nome, self.codigo_uf)


class Endereco(models.Model):
    municipio = models.ForeignKey(
                Municipios, verbose_name='Município',
                on_delete=models.CASCADE,
                help_text='Selecione o município')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a observação')

    numero = models.CharField(
             'Número', max_length=20,
             null=True, blank=True,
             help_text='Informe o numero')
    rua = models.CharField(
          'Rua', max_length=50,
          help_text='Informe a rua')
    bairro = models.CharField(
             'Bairro', max_length=50,
             help_text='Informe o bairro')
    complemento = models.TextField(
                  'Complemento',
                  help_text='Informe o complemento',
                  blank=True)
    latitude = models.FloatField(
               'Latitude', max_length=8,
               blank=True, null=True,
               help_text='Informe a Latitude')
    longitude = models.FloatField(
                'Longitude', max_length=8,
                blank=True, null=True,
                help_text='Informe a Longitude')

    datacriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
        'Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        db_table = 'endereco'

    def __str__(self):
        return '{}, {}, {}, {}'.format(
            self.rua, self.numero, self.bairro, self.municipio)
