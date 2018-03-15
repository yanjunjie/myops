# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0005_remove_app_subsys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='host',
        ),
    ]
