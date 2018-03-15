# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0075_weblogic_admin_servername'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblogic_admin',
            name='admin_status',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
    ]
