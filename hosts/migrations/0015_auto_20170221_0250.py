# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0014_auto_20170221_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='system_type',
            field=models.CharField(default=b'linux', max_length=32, choices=[(b'linux(vm)', b'Linux(VM)'), (b'linux(p)', b'Linux(P)')]),
        ),
    ]
