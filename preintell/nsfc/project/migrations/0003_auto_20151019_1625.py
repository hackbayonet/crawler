# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20151019_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Detail_abstract_english',
            field=models.CharField(max_length=5000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='Detail_abstract_chinese',
            field=models.CharField(max_length=2000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='Detail_achievement',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='Detail_keyword_chinese',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='Detail_keyword_english',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
