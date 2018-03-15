# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0027_auto_20170301_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_admin',
            name='primary',
        ),
        migrations.RemoveField(
            model_name='weblogic_admin',
            name='serverhost',
        ),
        migrations.DeleteModel(
            name='weblogic_admin',
        ),
    ]
