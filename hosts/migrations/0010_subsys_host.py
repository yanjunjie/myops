# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0009_auto_20170112_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsys',
            name='host',
            field=models.ManyToManyField(to='hosts.Host'),
        ),
    ]
