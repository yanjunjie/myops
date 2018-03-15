# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0030_auto_20170301_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='weblogic_admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('middleware', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6\xe5\x90\x8d', blank=True)),
                ('username', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('console_port', models.IntegerField(null=True, verbose_name=b'\xe6\x8e\xa7\xe5\x88\xb6\xe5\x8f\xb0\xe7\xab\xaf\xe5\x8f\xa3', blank=True)),
                ('cluster', models.CharField(max_length=30, null=True, verbose_name=b'\xe9\x9b\x86\xe7\xbe\xa4\xe5\x90\x8d', blank=True)),
                ('create_date', models.DateField(null=True, verbose_name=b'\xe5\xae\x89\xe8\xa3\x85\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('primary', models.ForeignKey(to='hosts.Host')),
                ('serverhost', models.ManyToManyField(to='hosts.weblogic_server')),
            ],
            options={
                'verbose_name': '\u63a7\u5236\u53f0\u90e8\u7f72\u4fe1\u606f',
                'managed': True,
                'verbose_name_plural': '\u63a7\u5236\u53f0\u90e8\u7f72\u4fe1\u606f',
            },
        ),
    ]
