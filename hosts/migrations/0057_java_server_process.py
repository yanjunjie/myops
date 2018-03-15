# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0056_remove_java_server_apppath'),
    ]

    operations = [
        migrations.AddField(
            model_name='java_server',
            name='process',
            field=models.ManyToManyField(to='hosts.java_process'),
        ),
    ]
