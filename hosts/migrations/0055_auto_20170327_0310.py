# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0054_java_process_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_server',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='java_process',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
