from django.db import models
from ocorrencia.models import Ocorrencia
from rat.models import RAT
from policial.models import Policial
from observacao.models import Observacao
from django.utils import timezone


def caminho_anexo(instance, filename):
    if instance.rat:
        rat = instance.rat
        filename = "RAT_" + str(rat.id) + "_" + str(timezone.now()) + "_" + filename

        pasta = f"RAT_{rat.id}"
    if instance.ocorrencia:
        ocorrencia = instance.ocorrencia
        filename = "OCORRENCIA_" + str(ocorrencia.id) + "_" + str(timezone.now()) + "_" + filename

        pasta = f"OCORRENCIA_{ocorrencia.id}"

    return f"anexos/{pasta}/{filename}"


class Anexo(models.Model):
    ocorrencia = models.ForeignKey(
                 Ocorrencia, verbose_name='Ocorrência',
                 on_delete=models.CASCADE,
                 null=True, blank=True,
                 help_text='Informe a ocorrência')
    rat = models.ForeignKey(
          RAT, verbose_name='Registro de Acidente de Trânsito',
          on_delete=models.CASCADE,
          null=True, blank=True,
          help_text='Informe o Registro de Acidente de Trânsito')
    policial = models.ForeignKey(
               Policial, verbose_name='Policial',
               on_delete=models.CASCADE,
               help_text='Informe o policial')
    observacao = models.ForeignKey(
                 Observacao, verbose_name='Observação',
                 on_delete=models.CASCADE,
                 help_text='Informe a observação')

    anexo = models.FileField(upload_to=caminho_anexo)

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Anexo'
        verbose_name_plural = 'Anexos'
        db_table = 'anexo'

    def __str__(self):
        return '{}'.format(self.observacao)
    
    def delete(self, *args, **kwargs):
        self.anexo.delete(save=False)

        super(Anexo, self).delete(*args, **kwargs)
