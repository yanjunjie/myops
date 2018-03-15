# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0045_java_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.IntegerField(null=True, verbose_name=b'\xe8\xbf\x9b\xe7\xa8\x8bID', blank=True)),
                ('path', models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('port', models.IntegerField(null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3', blank=True)),
                ('cpu', models.CharField(max_length=50, null=True, verbose_name=b'cpu', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
        ),
    ]
