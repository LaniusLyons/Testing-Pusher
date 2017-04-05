# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.SlugField(default=core.models.generate_slug, unique=True)),
                ('type', models.CharField(default=b'Us', max_length=2, choices=[(b'Us', b'Usuario'), (b'Ad', b'Administrador'), (b'Gd', b'Guardia')])),
            ],
            options={
                'db_table': 'Perfil',
            },
            bases=('auth.user',),
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
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='perfil',
            name='fk_universidad',
            field=models.ForeignKey(related_name='universidad', blank=True, to='core.Universidad', null=True),
            preserve_default=True,
        ),
    ]
