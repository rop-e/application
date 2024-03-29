# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('batalhao', '0001_initial'),
        ('guarnicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(help_text='Informe o cargo', max_length=50, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='PostoGraduacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postograduacao', models.CharField(help_text='Informe o posto ou gradução', max_length=40, verbose_name='Posto ou Graduação')),
            ],
            options={
                'verbose_name': 'Posto ou graduação',
                'verbose_name_plural': 'Postos ou graduações',
                'db_table': 'postograduacao',
                'ordering': ('postograduacao',),
            },
        ),
        migrations.CreateModel(
            name='TipoSanguineo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(help_text='Informe o tipo sanguíneo', max_length=2, verbose_name='Tipo Sanguíneo')),
                ('fatorRh', models.CharField(help_text='Informe o fator Rh', max_length=1, verbose_name='Fator Rh')),
            ],
            options={
                'verbose_name': 'Tipo sanguíneo',
                'verbose_name_plural': 'Tipos sanguíneos',
                'db_table': 'tiposanguineo',
            },
        ),
        migrations.CreateModel(
            name='Policial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeguerra', models.CharField(help_text='Informe o nome de guerra', max_length=50, verbose_name='Nome de Guerra')),
                ('dtpraca', models.DateField(verbose_name='Data de praça')),
                ('foto', models.ImageField(blank=True, default='imagens_perfil/perfil.png', null=True, upload_to='imagens_perfil')),
                ('batalhao', models.ForeignKey(help_text='Informe o batalhão', on_delete=django.db.models.deletion.CASCADE, to='batalhao.Batalhao', verbose_name='Batalhão')),
                ('cargo', models.ForeignKey(help_text='Informe o cargo', on_delete=django.db.models.deletion.CASCADE, to='policial.Cargo', verbose_name='Cargo')),
                ('companhia', models.ForeignKey(help_text='Informe a companhia', on_delete=django.db.models.deletion.CASCADE, related_name='policial_companhia', to='guarnicao.Companhia', verbose_name='Companhia')),
                ('matricula', models.OneToOneField(help_text='Informe a matrícula', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Matrícula')),
                ('postograduacao', models.ForeignKey(help_text='Informe o posto ou graduação', on_delete=django.db.models.deletion.CASCADE, to='policial.PostoGraduacao', verbose_name='Posto ou graduação')),
                ('tiposanguineo', models.ForeignKey(help_text='Informe o tipo sanguíneo', on_delete=django.db.models.deletion.CASCADE, to='policial.TipoSanguineo', verbose_name='Tipo Sanguíneo')),
            ],
            options={
                'verbose_name': 'Policial',
                'verbose_name_plural': 'Policiais',
                'db_table': 'policial',
            },
        ),
    ]
