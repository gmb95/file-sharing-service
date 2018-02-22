# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profilefile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefile',
            old_name='file_way',
            new_name='image',
        ),
    ]
