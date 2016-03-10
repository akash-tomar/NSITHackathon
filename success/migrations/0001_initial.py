# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Percentage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('percentage', models.CharField(max_length=100, default=0)),
                ('no_users', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('v_id', models.IntegerField(default=0)),
                ('hit', models.BigIntegerField(default=0)),
                ('success', models.BigIntegerField(default=0)),
                ('number', models.BigIntegerField(default=0)),
            ],
        ),
    ]
