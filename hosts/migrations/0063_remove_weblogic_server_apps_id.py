# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0062_auto_20170327_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_server',
            name='apps_id',
        ),
    ]
