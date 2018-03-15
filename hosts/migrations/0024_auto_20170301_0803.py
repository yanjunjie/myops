# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0023_weblogic_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_server',
            name='admin_id',
        ),
        migrations.RemoveField(
            model_name='weblogic_server',
            name='apps_id',
        ),
        migrations.RemoveField(
            model_name='weblogic_server',
            name='managed_server_id',
        ),
        migrations.DeleteModel(
            name='weblogic_admin',
        ),
        migrations.DeleteModel(
            name='weblogic_server',
        ),
    ]
