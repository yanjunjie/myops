# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0032_middleware'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblogic_admin',
            name='middleware',
            field=models.ForeignKey(to='hosts.middleware'),
        ),
    ]
