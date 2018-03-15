# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0078_auto_20170620_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True)),
                ('release', models.TextField(null=True)),
                ('version', models.TextField(null=True)),
                ('machine', models.TextField(null=True)),
                ('cpu', models.IntegerField(null=True)),
                ('memory', models.IntegerField(null=True)),
                ('swap', models.IntegerField(null=True)),
                ('server', models.OneToOneField(to='hosts.Host')),
            ],
        ),
    ]
