# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0007_auto_20170112_0618'),
    ]

    operations = [
        migrations.DeleteModel(
            name='App',
        ),
        migrations.DeleteModel(
            name='Subsys',
        ),
    ]
