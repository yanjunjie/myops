# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_auto_20170105_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('memo', models.TextField(null=True, blank=True)),
                ('host', models.ManyToManyField(to='hosts.Host')),
            ],
            options={
                'verbose_name': '\u5e94\u7528',
                'verbose_name_plural': '\u5e94\u7528',
            },
        ),
        migrations.CreateModel(
            name='Subsys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u5b50\u7cfb\u7edf',
                'verbose_name_plural': '\u5b50\u7cfb\u7edf',
            },
        ),
        migrations.AddField(
            model_name='app',
            name='subsys',
            field=models.ManyToManyField(to='hosts.Subsys'),
        ),
    ]
