# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0055_auto_20170327_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_server',
            name='apppath',
        ),
    ]
