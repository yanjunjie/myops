# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0074_auto_20170519_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblogic_admin',
            name='servername',
            field=models.CharField(default=b'AdminServer', max_length=200, null=True, verbose_name=b'\xe5\xae\x9e\xe4\xbe\x8b\xe5\x90\x8d', blank=True),
        ),
    ]
