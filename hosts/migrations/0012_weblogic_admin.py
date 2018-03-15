# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0011_auto_20170209_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='weblogic_admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.CharField(max_length=20, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe4\xb8\xbb\xe6\x9c\xba', blank=True)),
                ('middleware', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6\xe5\x90\x8d', blank=True)),
                ('username', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('console_port', models.IntegerField(null=True, verbose_name=b'\xe6\x8e\xa7\xe5\x88\xb6\xe5\x8f\xb0\xe7\xab\xaf\xe5\x8f\xa3', blank=True)),
                ('cluster', models.CharField(max_length=30, null=True, verbose_name=b'\xe9\x9b\x86\xe7\xbe\xa4\xe5\x90\x8d', blank=True)),
                ('create_date', models.DateField(null=True, verbose_name=b'\xe5\xae\x89\xe8\xa3\x85\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('status', models.CharField(max_length=20, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('server_hostid', models.ManyToManyField(to='hosts.Host')),
            ],
            options={
                'verbose_name': '\u90e8\u7f72\u4fe1\u606f',
                'managed': True,
                'verbose_name_plural': '\u90e8\u7f72\u4fe1\u606f',
            },
        ),
    ]
