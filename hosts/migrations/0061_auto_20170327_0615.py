# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0060_java_server_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_server',
            name='process',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='status',
        ),
        migrations.AlterField(
            model_name='java_process',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='java_server',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
