# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0067_auto_20170327_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='java_process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('pid', models.IntegerField(null=True, verbose_name=b'\xe8\xbf\x9b\xe7\xa8\x8bID', blank=True)),
                ('path', models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('port', models.IntegerField(null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3', blank=True)),
                ('cpu', models.CharField(max_length=50, null=True, verbose_name=b'cpu', blank=True)),
                ('date', models.DateField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('host', models.ForeignKey(to='hosts.Host')),
            ],
        ),
        migrations.CreateModel(
            name='java_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('app', models.ForeignKey(to='hosts.App')),
                ('process', models.ManyToManyField(to='hosts.java_process')),
            ],
        ),
    ]
