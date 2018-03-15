# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0017_remove_weblogic_server_apps_id'),
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
        migrations.RemoveField(
            model_name='weblogic_admin',
            name='server_hostid',
        ),
    ]
