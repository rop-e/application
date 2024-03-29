# Generated by Django 3.0.5 on 2020-08-13 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('observacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(help_text='Informe o modelo', max_length=80, verbose_name='Modelo')),
                ('ano', models.IntegerField(help_text='Informe o ano', verbose_name='Ano')),
                ('numero_viatura', models.CharField(help_text='Informe a identificação da viatura', max_length=10, unique=True, verbose_name='Identificação da viatura')),
                ('status', models.CharField(choices=[('operacional', 'OPERACIONAL'), ('manutencao', 'EM MANUTENÇÃO'), ('parado', 'PARADO')], help_text='Informe o status', max_length=15, verbose_name='Status')),
                ('placa', models.CharField(help_text='Informe a placa', max_length=10, verbose_name='Placa')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('observacao', models.ForeignKey(blank=True, help_text='Informe a observação', null=True, on_delete=django.db.models.deletion.CASCADE, to='observacao.Observacao', verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Viatura',
                'verbose_name_plural': 'Viaturas',
                'db_table': 'viatura',
            },
        ),
    ]
