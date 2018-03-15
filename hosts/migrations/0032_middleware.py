# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0031_weblogic_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='middleware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6\xe5\x90\x8d', blank=True)),
                ('version', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xad\xe9\x97\xb4\xe4\xbb\xb6\xe7\x89\x88\xe6\x9c\xac', blank=True)),
            ],
            options={
                'verbose_name': '\u4e2d\u95f4\u4ef6',
                'managed': True,
                'verbose_name_plural': '\u4e2d\u95f4\u4ef6',
            },
        ),
    ]
