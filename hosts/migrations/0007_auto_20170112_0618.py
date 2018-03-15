# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0006_remove_app_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='app',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subsys',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='subsys',
            name='name',
        ),
    ]
