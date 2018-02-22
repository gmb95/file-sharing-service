# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150521_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilefile',
            name='description',
        ),
        migrations.AddField(
            model_name='profilefile',
            name='text',
            field=models.TextField(default=1234, max_length=256),
            preserve_default=False,
        ),
    ]
