from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

SEXO = (
    ('M', 'MASCULINO'),
    ('F', 'FEMININO')
)


class GerenciarPerfilUsuario(BaseUserManager):
    """Modelo de usuario personalizado"""
    def create_user(self, nome, sexo, cpf, matricula,
                    email, dtnascimento, password=None):
        """Criar novo usuário"""

        if not matricula:
            raise ValueError('O usuário deve informar a sua matrícula!')
        elif not email:
            raise ValueError('O usuário deve informar um e-mail!')

        email = self.normalize_email(email)
        usuario = self.model(
                  email=email, nome=nome, sexo=sexo,
                  cpf=cpf, matricula=matricula,
                  dtnascimento=dtnascimento)

        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, nome, sexo, cpf, matricula,
                         email, dtnascimento, password=None):
        """Criar superusuário"""

        usuario = self.create_user(
                  email=email, nome=nome, sexo=sexo,
                  cpf=cpf, matricula=matricula,
                  dtnascimento=dtnascimento)

        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario


class AbstractUsuario(AbstractBaseUser, PermissionsMixin):
    """Representa um "perfil de usuário" dentro do nosso sistema."""
    nome = models.CharField(
           'Nome', max_length=100,
           help_text='Informe o nome')
    sexo = models.CharField(
           'Sexo', max_length=1, choices=SEXO,
           help_text='Informe o sexo')
    email = models.CharField(
            'E-mail', max_length=255,
            unique=True, help_text='Informe o e-mail')
    dtnascimento = models.DateField('Data de nascimento')
    cpf = models.CharField(
          'CPF', max_length=14, unique=True,
          help_text='Informe o CPF')
    matricula = models.CharField(
                'Matrícula', max_length=14, unique=True,
                help_text='Informe a matrícula')

    is_active = models.BooleanField(
                verbose_name='Está ativo?',
                default=True)
    is_staff = models.BooleanField(
               verbose_name='Administrador',
               default=False)

    objects = GerenciarPerfilUsuario()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = [
        'nome',
        'sexo',
        'email',
        'dtnascimento',
        'cpf'
    ]

    datacriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataatualizacao = models.DateTimeField(
                      'Data de atualização', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} - {}'.format(self.matricula, self.nome)


class Usuario(AbstractUsuario):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'contasdeusuario'
