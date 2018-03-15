# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0070_web_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_server',
            name='date',
            field=models.DateField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
