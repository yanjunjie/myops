# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0040_auto_20170324_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\x90\x8d', blank=True)),
            ],
        ),
    ]
