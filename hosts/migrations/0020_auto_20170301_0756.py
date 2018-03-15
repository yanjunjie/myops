# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0019_delete_weblogic_admin_server_hostid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_server',
            name='admin_id',
        ),
        migrations.DeleteModel(
            name='weblogic_server',
        ),
    ]
