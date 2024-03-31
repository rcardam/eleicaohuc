# Generated by Django 5.0.3 on 2024-03-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(blank=True, max_length=8, null=True)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('dtvoto', models.DateTimeField(auto_now_add=True, null=True)),
                ('voto', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Eleição',
                'verbose_name_plural': 'Eleições',
                'db_table': 'votacao',
            },
        ),
    ]
