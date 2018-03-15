# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0043_java_server_server_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_server',
            name='apps_id',
        ),
        migrations.RemoveField(
            model_name='java_server',
            name='java_server_id',
        ),
        migrations.DeleteModel(
            name='java_server',
        ),
    ]
