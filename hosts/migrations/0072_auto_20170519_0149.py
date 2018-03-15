# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0071_web_server_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web_server',
            name='host',
        ),
        migrations.RemoveField(
            model_name='web_server',
            name='type',
        ),
        migrations.DeleteModel(
            name='web_server',
        ),
    ]
