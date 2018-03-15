# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0051_java_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('apppath', models.ForeignKey(to='hosts.java_process')),
                ('apps', models.ForeignKey(to='hosts.App')),
            ],
        ),
    ]
