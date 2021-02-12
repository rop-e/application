from django.db import models
from django.core.exceptions import ValidationError


class Aplicacao(models.Model):
    versao = models.CharField("Versão da aplicação", max_length=10, help_text="Informe a versão da aplicação")
    datalancamento = models.DateField("Data de lançamento")
    descricao = models.TextField("Descrição")
    atual = models.BooleanField(verbose_name="Atual", default=False)

    datacriacao = models.DateTimeField("Data de criação", auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      "Data de atualização", auto_now=True)

    class Meta:
        verbose_name = "Aplicação"
        verbose_name_plural = "Aplicações"
        db_table = "aplicacao"

    def __str__(self):
        ativa = "MAIS ATUAL" if self.atual else "DESATUALIZADA"
        return "{} - {}".format(self.versao, ativa)
    
    def save(self, *args, **kwargs):
        if self.atual:
            if Aplicacao.objects.filter(atual=True):
                raise ValidationError("Já existe versão atual, desmarque a opção!", code="aplicacao")

        super(Aplicacao, self).save(*args, **kwargs)
