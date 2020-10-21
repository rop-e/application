from django.db import models
from endereco.models import Endereco

SEXO = (
    ('M', 'MASCULINO'),
    ('F', 'FEMININO')
)


class Pessoa(models.Model):
    nome = models.CharField(
           'Nome', max_length=50,
           help_text='Informe o nome')
    sexo = models.CharField(
           'Sexo', max_length=1,
           choices=SEXO, help_text='Informe o sexo')
    datanascimento = models.DateField(
                     'Data de nascimento', blank=True, null=True,
                     help_text='Informe a data de nascimento')
    mae = models.CharField(
          'Nome da mãe', max_length=50, blank=True,
          help_text='Informe o nome da mãe')
    apelido = models.CharField(
              'Apelido', max_length=25, blank=True,
              help_text='Informe o apelido')
    cpf = models.CharField(
          'CPF', max_length=14, blank=True,
          help_text='Informe o CPF')
    rg = models.CharField(
         'RG', max_length=14, blank=True,
         help_text='Informe o RG')
    cnh = models.CharField(
          'CNH', max_length=30, blank=True,
          help_text='Informe a CNH')
    datavencimentocnh = models.DateField(
                        'Data de vencimento da CNH',
                        blank=True, null=True,
                        help_text='Informe a data de vencimento da CNH')
    categoriacnh = models.CharField(
                   'Categoria da CNH', max_length=5,
                   null=True, blank=True,
                   help_text='Informe a categoria da CNH')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

    def __str__(self):
        return self.nome


class PessoaEndereco(models.Model):
    pessoa = models.ForeignKey(
             Pessoa, verbose_name='Pessoa',
             on_delete=models.CASCADE,
             help_text='Informe a pessoa')
    endereco = models.ForeignKey(
               Endereco, verbose_name='Endereço',
               on_delete=models.CASCADE,
               help_text='Informe o endereço')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Endereço de pessoa'
        verbose_name_plural = 'Endereços de pessoa'
        db_table = 'pessoaendereco'

    def __str__(self):
        return '{} - {}'.format(self.pessoa, self.endereco)
