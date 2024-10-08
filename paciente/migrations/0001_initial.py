# Generated by Django 5.1 on 2024-09-09 20:34

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.usuario')),
                ('plano_saude', models.CharField(blank=True, max_length=100, null=True)),
                ('numero_cartao_sus', models.CharField(blank=True, max_length=15, null=True)),
                ('alergias', models.TextField(blank=True, null=True)),
                ('historico_medico', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['first_name'],
            },
            bases=('usuario.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
