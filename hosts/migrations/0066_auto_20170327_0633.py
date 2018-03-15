# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0065_remove_fuck_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_server',
            name='managed_server_id',
        ),
        migrations.RemoveField(
            model_name='weblogic_admin',
            name='serverhost',
        ),
        migrations.DeleteModel(
            name='weblogic_server',
        ),
    ]
