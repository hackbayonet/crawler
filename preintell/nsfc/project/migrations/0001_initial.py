# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Project_pid', models.IntegerField(max_length=10)),
                ('Project_name', models.CharField(max_length=100)),
                ('Project_classify', models.CharField(max_length=50)),
                ('Project_person', models.CharField(max_length=50)),
                ('Project_department', models.CharField(max_length=50)),
                ('Project_money', models.CharField(max_length=30)),
                ('Project_time', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
