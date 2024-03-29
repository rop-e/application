# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgenteRecebedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_agente', models.CharField(help_text='Informe o nome', max_length=30, verbose_name='Nome do agente')),
                ('cargo', models.CharField(help_text='Informe o cargo', max_length=20, verbose_name='Cargo')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Agente recebedor',
                'verbose_name_plural': 'Agentes recebedores',
                'db_table': 'agenterecebedor',
            },
        ),
        migrations.CreateModel(
            name='LocalRecebedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(help_text='Informe o local recebedor', max_length=30, verbose_name='Local recebedor')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Local recebedor',
                'verbose_name_plural': 'Locais recebedores',
                'db_table': 'localrecebedor',
            },
        ),
    ]
