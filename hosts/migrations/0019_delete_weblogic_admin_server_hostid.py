# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0018_auto_20170301_0734'),
    ]

    operations = [
        migrations.DeleteModel(
            name='weblogic_admin_server_hostid',
        ),
    ]
