# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150520_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilefile',
            name='name_of_user',
        ),
        migrations.AddField(
            model_name='profilefile',
            name='description',
            field=models.CharField(default=1234, max_length=256),
            preserve_default=False,
        ),
    ]
