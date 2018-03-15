# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0010_subsys_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='package',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='app',
            name='path',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
    ]
