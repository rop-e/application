# Generated by Django 3.0.5 on 2020-10-05 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policial', '0001_initial'),
        ('guarnicao', '0011_guarnicao_observacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('dataatualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('guarnicao_nova', models.ForeignKey(help_text='Informe a nova guarnição', on_delete=django.db.models.deletion.CASCADE, related_name='permuta_guarnicaonova', to='guarnicao.Guarnicao', verbose_name='Nova guarnição')),
                ('guarnicao_ultima', models.ForeignKey(help_text='Informe a última guarnição', on_delete=django.db.models.deletion.CASCADE, related_name='permuta_guarnicaoultima', to='guarnicao.Guarnicao', verbose_name='Última guarnição')),
                ('policial', models.ForeignKey(help_text='Informe quem é o policial', on_delete=django.db.models.deletion.CASCADE, to='policial.Policial', verbose_name='Policial permutado')),
            ],
            options={
                'verbose_name': 'Permuta',
                'verbose_name_plural': 'Permutas',
                'db_table': 'permuta',
            },
        ),
    ]