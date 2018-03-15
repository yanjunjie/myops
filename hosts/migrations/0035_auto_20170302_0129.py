# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0034_app_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblogic_admin',
            name='username',
            field=models.ForeignKey(to='hosts.app_user'),
        ),
    ]
