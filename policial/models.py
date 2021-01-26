from django.db import models
from contasdeusuario.models import Usuario
from PIL import Image
from batalhao.models import Batalhao
import os
from django.utils import timezone
from ropd.settings import MEDIA_ROOT


def caminho_imagens_perfil(instance, filename):
    if not instance.dataatualizacao:
        data = timezone.now()
    else:
        data = instance.dataatualizacao

    filename = "PERFIL_USUARIO_" + str(instance.matricula.id) + "_" + str(data.strftime("%d-%m-%Y_%H-%M-%S")) + "." + filename.split('.')[-1]

    return f"imagens_perfil/{filename}"


class PostoGraduacao(models.Model):
    postograduacao = models.CharField(
                     'Posto ou Graduação', max_length=40,
                     help_text='Informe o posto ou gradução')

    class Meta:
        verbose_name = 'Posto ou graduação'
        verbose_name_plural = 'Postos ou graduações'
        db_table = 'postograduacao'
        ordering = ('postograduacao',)

    def __str__(self):
        return self.postograduacao


class Cargo(models.Model):
    cargo = models.CharField(
            'Cargo', max_length=50,
            help_text='Informe o cargo')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'

    def __str__(self):
        return self.cargo


class TipoSanguineo(models.Model):
    grupo = models.CharField(
            'Tipo Sanguíneo', max_length=2,
            help_text='Informe o tipo sanguíneo')
    fatorRh = models.CharField(
              'Fator Rh', max_length=1,
              help_text='Informe o fator Rh')

    class Meta:
        verbose_name = 'Tipo sanguíneo'
        verbose_name_plural = 'Tipos sanguíneos'
        db_table = 'tiposanguineo'

    def __str__(self):
        return '{}{}'.format(self.grupo, self.fatorRh)


class Policial(models.Model):
    postograduacao = models.ForeignKey(
                     PostoGraduacao,
                     verbose_name='Posto ou graduação',
                     on_delete=models.CASCADE,
                     help_text='Informe o posto ou graduação')
    cargo = models.ForeignKey(
            Cargo, verbose_name='Cargo',
            on_delete=models.CASCADE,
            help_text='Informe o cargo')
    tiposanguineo = models.ForeignKey(
                    TipoSanguineo, verbose_name='Tipo Sanguíneo',
                    on_delete=models.CASCADE,
                    help_text='Informe o tipo sanguíneo')
    matricula = models.OneToOneField(
                Usuario, verbose_name='Matrícula',
                on_delete=models.CASCADE,
                help_text='Informe a matrícula')
    batalhao = models.ForeignKey(
               Batalhao, verbose_name='Batalhão',
               on_delete=models.CASCADE,
               help_text='Informe o batalhão')
    companhia = models.ForeignKey(
                'guarnicao.Companhia', verbose_name='Companhia',
                on_delete=models.CASCADE,
                related_name='policial_companhia',
                help_text='Informe a companhia')

    nomeguerra = models.CharField(
                 'Nome de Guerra', max_length=50,
                 help_text='Informe o nome de guerra')
    dtpraca = models.DateField('Data de praça')
    foto = models.ImageField(
           upload_to=caminho_imagens_perfil,
           null=True, blank=True,
           default='imagens_perfil/perfil.png')
    
    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Policial'
        verbose_name_plural = 'Policiais'
        db_table = 'policial'

    def __str__(self):
        return '{} {}'.format(self.postograduacao, self.nomeguerra)

    def save(self, *args, **kwargs):
        if not self.foto:
            self.foto = "imagens_perfil/perfil.png"

        super(Policial, self).save(*args, **kwargs)

        imagem = Image.open(self.foto.path)

        if imagem.height > 300 or imagem.width > 300:
            output_size = (300, 300)
            imagem.thumbnail(output_size, Image.ANTIALIAS)
            imagem.save(self.foto.path, format="JPEG", quality=100)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.foto.path):
            if not self.foto == "imagens_perfil/perfil.png":
                os.remove(self.foto.path)
        
        path = MEDIA_ROOT + "imagens_perfil/"

        for file in os.listdir(path):
            if file.startswith("PERFIL_USUARIO_" + str(self.matricula.id) + "_"):
                os.remove(path + file)

        super(Policial, self).delete(*args,**kwargs)

