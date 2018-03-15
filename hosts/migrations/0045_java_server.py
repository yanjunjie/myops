# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0044_auto_20170324_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\x90\x8d', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('apps', models.ForeignKey(to='hosts.App')),
                ('host', models.ForeignKey(to='hosts.Host')),
            ],
        ),
    ]
