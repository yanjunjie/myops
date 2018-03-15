# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0076_weblogic_admin_admin_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblogic_server',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
