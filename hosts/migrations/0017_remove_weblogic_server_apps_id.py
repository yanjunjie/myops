# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0016_weblogic_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_server',
            name='apps_id',
        ),
    ]
