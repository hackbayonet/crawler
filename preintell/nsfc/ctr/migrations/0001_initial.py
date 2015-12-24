# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ctr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Ctr_name', models.CharField(max_length=255)),
                ('Ctr_id', models.CharField(max_length=20)),
                ('Ctr_stitle', models.CharField(max_length=255)),
                ('Ctr_applicant', models.CharField(max_length=50)),
                ('Ctr_leader', models.CharField(max_length=50)),
                ('Ctr_status', models.CharField(max_length=20)),
                ('Ctr_sponsor', models.CharField(max_length=100)),
                ('Ctr_type', models.CharField(max_length=20)),
                ('Ctr_html', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
