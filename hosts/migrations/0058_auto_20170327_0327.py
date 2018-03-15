# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0057_java_server_process'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_server',
            name='apps',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='process',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='status',
        ),
    ]
