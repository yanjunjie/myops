# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20170112_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='subsys',
        ),
    ]
