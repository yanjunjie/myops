# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0072_auto_20170519_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='web_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xae\x9e\xe4\xbe\x8b\xe5\x90\x8d', blank=True)),
                ('project', models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe5\x8d\x95\xe5\x85\x83', blank=True)),
                ('path', models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('date', models.DateField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('status', models.CharField(max_length=50, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('host', models.ForeignKey(to='hosts.Host')),
                ('type', models.ForeignKey(to='hosts.middleware')),
            ],
        ),
    ]
