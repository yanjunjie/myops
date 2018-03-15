# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0058_auto_20170327_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_server',
            name='status',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
    ]
