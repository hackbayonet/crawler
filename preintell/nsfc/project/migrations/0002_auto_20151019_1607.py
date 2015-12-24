# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('Detail_pid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('Detail_name', models.CharField(max_length=100)),
                ('Detail_classify', models.CharField(max_length=50)),
                ('Detail_apply', models.CharField(max_length=20)),
                ('Detail_person', models.CharField(max_length=50)),
                ('Detail_job', models.CharField(max_length=50)),
                ('Detail_department', models.CharField(max_length=50)),
                ('Detail_time', models.CharField(max_length=50)),
                ('Detail_money', models.CharField(max_length=50)),
                ('Detail_abstract_chinese', models.CharField(max_length=1500, null=True)),
                ('Detail_keyword_chinese', models.CharField(max_length=255, null=True)),
                ('Detail_keyword_english', models.CharField(max_length=255, null=True)),
                ('Detail_abstract_end', models.CharField(max_length=5000, null=True)),
                ('Detail_achievement', models.CharField(max_length=3000, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_pid',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
