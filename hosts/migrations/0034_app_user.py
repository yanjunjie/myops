# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0033_auto_20170302_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='app_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('middleware', models.ManyToManyField(to='hosts.middleware')),
            ],
            options={
                'verbose_name': '\u4e2d\u95f4\u4ef6\u7528\u6237',
                'managed': True,
                'verbose_name_plural': '\u4e2d\u95f4\u4ef6\u7528\u6237',
            },
        ),
    ]
