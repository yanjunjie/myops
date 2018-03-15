# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0077_auto_20170620_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblogic_admin',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='java_process',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='web_server',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='weblogic_admin',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe5\xae\x89\xe8\xa3\x85\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='zk_server',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
