# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0037_auto_20170302_0220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='weblogic_admin_server_hostid',
        ),
    ]
