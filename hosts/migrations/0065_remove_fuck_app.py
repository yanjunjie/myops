# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0064_fuck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuck',
            name='app',
        ),
    ]
