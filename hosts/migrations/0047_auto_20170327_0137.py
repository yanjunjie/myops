# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0046_java_process'),
    ]

    operations = [
        migrations.DeleteModel(
            name='java_process',
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
            name='java_server',
        ),
    ]
