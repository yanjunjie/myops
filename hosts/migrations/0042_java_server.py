# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0041_java_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\x90\x8d', blank=True)),
                ('apps_id', models.ForeignKey(to='hosts.App')),
                ('java_server_id', models.ForeignKey(to='hosts.Host')),
            ],
        ),
    ]
