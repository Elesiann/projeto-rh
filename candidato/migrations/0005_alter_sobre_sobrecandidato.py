# Generated by Django 3.2.6 on 2021-08-25 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidato', '0004_sobre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre',
            name='sobrecandidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
