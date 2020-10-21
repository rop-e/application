from django.db import models


class LocalRecebedor(models.Model):
    local = models.CharField(
            'Local recebedor', max_length=30,
            help_text='Informe o local recebedor')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Local recebedor'
        verbose_name_plural = 'Locais recebedores'
        db_table = 'localrecebedor'

    def __str__(self):
        return self.local


class AgenteRecebedor(models.Model):
    nome_agente = models.CharField(
                  'Nome do agente', max_length=30,
                  help_text='Informe o nome')
    cargo = models.CharField(
            'Cargo', max_length=20,
            help_text='Informe o cargo')

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Agente recebedor'
        verbose_name_plural = 'Agentes recebedores'
        db_table = 'agenterecebedor'

    def __str__(self):
        return '{} - {}'.format(self.nome_agente, self.cargo)
