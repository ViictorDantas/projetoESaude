# Generated by Django 5.1 on 2024-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='rua',
            field=models.CharField(max_length=255),
        ),
    ]