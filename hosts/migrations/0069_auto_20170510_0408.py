# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0068_java_process_java_server'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='java_process',
            options={'managed': True, 'verbose_name': 'java\u90e8\u7f72\u4fe1\u606f', 'verbose_name_plural': 'java\u90e8\u7f72\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='java_server',
            options={'managed': True, 'verbose_name': 'java\u540e\u53f0\u8fdb\u7a0b', 'verbose_name_plural': 'java\u540e\u53f0\u8fdb\u7a0b'},
        ),
        migrations.AddField(
            model_name='weblogic_admin',
            name='server_status',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
    ]
