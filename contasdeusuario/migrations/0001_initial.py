# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nome', models.CharField(help_text='Informe o nome', max_length=100, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], help_text='Informe o sexo', max_length=1, verbose_name='Sexo')),
                ('email', models.CharField(help_text='Informe o e-mail', max_length=255, unique=True, verbose_name='E-mail')),
                ('dtnascimento', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.CharField(help_text='Informe o CPF', max_length=14, unique=True, verbose_name='CPF')),
                ('matricula', models.CharField(help_text='Informe a matrícula', max_length=14, unique=True, verbose_name='Matrícula')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Administrador')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'contasdeusuario',
            },
        ),
    ]
