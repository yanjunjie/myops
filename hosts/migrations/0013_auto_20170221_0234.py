# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0012_weblogic_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weblogic_admin',
            name='status',
        ),
        migrations.AddField(
            model_name='weblogic_admin',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
