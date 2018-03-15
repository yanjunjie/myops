# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0042_java_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_server',
            name='server_port',
            field=models.IntegerField(null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3', blank=True),
        ),
    ]
