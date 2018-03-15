# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0049_java_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_server',
            name='apppath',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='apps',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='host',
        ),
        migrations.DeleteModel(
            name='java_process',
        ),
        migrations.DeleteModel(
            name='java_server',
        ),
    ]
