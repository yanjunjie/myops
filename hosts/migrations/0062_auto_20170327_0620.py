# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0061_auto_20170327_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='java_process',
            name='host',
        ),
        migrations.DeleteModel(
            name='java_server',
        ),
        migrations.DeleteModel(
            name='java_process',
        ),
    ]
