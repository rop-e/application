from django.db import models
from endereco.models import Municipios


class Batalhao(models.Model):
    batalhao = models.CharField(
              'Batalhão', max_length=100,
              help_text='Informe o Batalhão')
    comandante = models.ForeignKey(
                 'policial.Policial',
                 verbose_name='Comandante',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 related_name="comandante_batalhao",
                 help_text='Informe o comandante do BPM')

    class Meta:
        verbose_name = 'Batalhão'
        verbose_name_plural = 'Batalhões'
        db_table = 'batalhao'

    def __str__(self):
        return self.batalhao


class BatalhaoMunicipios(models.Model):
    batalhao = models.ForeignKey(
               Batalhao,
               verbose_name='Batalhão',
               on_delete=models.CASCADE,
               help_text='Informe o Batalhão')
    municipio = models.ForeignKey(
                Municipios,
                verbose_name='Município',
                on_delete=models.CASCADE,
                help_text='Informe o Município')

    class Meta:
        verbose_name = 'Municipios do Batalhão'
        verbose_name_plural = 'Municipios dos Batalhões'
        db_table = 'batalhaomunicipios'

    def __str__(self):
        return '{} - {}'.format(self.municipio, self.batalhao)
