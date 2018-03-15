# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0053_java_process_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_process',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
