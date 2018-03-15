# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0026_weblogic_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='weblogic_admin_server_hostid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weblogic_admin_id', models.IntegerField(default=11)),
                ('host_id', models.IntegerField(default=11)),
            ],
        ),
        migrations.AlterModelOptions(
            name='weblogic_admin',
            options={'managed': True, 'verbose_name': '\u63a7\u5236\u53f0\u90e8\u7f72\u4fe1\u606f', 'verbose_name_plural': '\u63a7\u5236\u53f0\u90e8\u7f72\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='weblogic_admin',
            name='primary',
            field=models.ForeignKey(to='hosts.Host'),
        ),
    ]
