# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Companero',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(default=core.models.generate_slug, unique=True)),
            ],
            options={
                'db_table': 'Companero',
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(default=core.models.generate_slug, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('aprobado', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Universidad',
            },
        ),
        migrations.AddField(
            model_name='companero',
            name='id_universidad',
            field=models.ForeignKey(to='core.Universidad'),
        ),
        migrations.AddField(
            model_name='companero',
            name='id_usuario_dos',
            field=models.ForeignKey(related_name='companero', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companero',
            name='id_usuario_uno',
            field=models.ForeignKey(related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
