# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0066_auto_20170327_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='weblogic_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xae\x9e\xe4\xbe\x8b\xe5\x90\x8d', blank=True)),
                ('server_port', models.IntegerField(null=True, verbose_name=b'\xe5\xae\x9e\xe4\xbe\x8b\xe7\xab\xaf\xe5\x8f\xa3', blank=True)),
                ('server_status', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('date', models.DateField(null=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('apps_id', models.ForeignKey(to='hosts.App')),
                ('managed_server_id', models.ForeignKey(to='hosts.Host')),
            ],
            options={
                'verbose_name': 'weblogic\u5b9e\u4f8b\u90e8\u7f72\u4fe1\u606f',
                'managed': True,
                'verbose_name_plural': 'weblogic\u5b9e\u4f8b\u90e8\u7f72\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='weblogic_admin',
            name='serverhost',
            field=models.ManyToManyField(to='hosts.weblogic_server'),
        ),
    ]
