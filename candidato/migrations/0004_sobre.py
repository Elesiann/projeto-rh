# Generated by Django 3.2.6 on 2021-08-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0003_alter_registro_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobrecandidato', models.TextField()),
            ],
        ),
    ]