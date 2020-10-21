from django.db import models
from contasdeusuario.models import Usuario
from PIL import Image
from batalhao.models import Batalhao


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
           upload_to='imagens_perfil',
           null=True, blank=True,
           default='imagens_perfil/perfil.png')

    class Meta:
        verbose_name = 'Policial'
        verbose_name_plural = 'Policiais'
        db_table = 'policial'

    def __str__(self):
        return '{} {}'.format(self.postograduacao, self.nomeguerra)

    def save(self, *args, **kwargs):
        super(Policial, self).save(*args, **kwargs)

        imagem = Image.open(self.foto.path)

        if imagem.height > 300 or imagem.width > 300:
            output_size = (300, 300)
            imagem.thumbnail(output_size)
            imagem.save(self.foto.path)
