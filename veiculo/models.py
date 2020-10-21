from django.db import models


class CategoriaVeiculo(models.Model):
    categoria = models.CharField(
                'Categoria', max_length=50,
                help_text='Informe a categoria')

    class Meta:
        verbose_name = 'Categoria de veículo'
        verbose_name_plural = 'Categorias de veículo'
        db_table = 'categoriaveiculo'

    def __str__(self):
        return self.categoria


class MarcaVeiculo(models.Model):
    marca = models.CharField(
            'Marca', max_length=50,
            help_text='Informe a marca')

    class Meta:
        verbose_name = 'Marca de veículo'
        verbose_name_plural = 'Marcas de veículo'
        db_table = 'marcaveiculo'

    def __str__(self):
        return self.marca


class Veiculo(models.Model):
    categoria = models.ForeignKey(
                CategoriaVeiculo,
                verbose_name='Categoria',
                on_delete=models.CASCADE,
                help_text='Informe a categoria')
    marca = models.ForeignKey(
            MarcaVeiculo,
            verbose_name='Marca',
            on_delete=models.CASCADE,
            help_text='Informe a marca')

    modelo = models.CharField(
             'Modelo', max_length=80,
             help_text='Informe o modelo')
    cor = models.CharField(
          'Cor', max_length=10, help_text='Informe a cor')
    chassi = models.CharField(
             'Chassi', max_length=30, blank=True,
             null=True, help_text='Informe o chassi')
    placa = models.CharField(
            'Placa', max_length=10, blank=True,
            null=True, help_text='Informe a placa')
    ano = models.IntegerField(
          'Ano', blank=True, null=True,
          help_text='Informe o ano')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        db_table = 'veiculo'

    def __str__(self):
        if self.placa:
            return '{} {} - ({})'.format(self.marca, self.modelo, self.placa)
        else:
            return '{} {}'.format(self.marca, self.modelo)
