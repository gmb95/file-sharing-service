# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_way', models.FileField(upload_to=b'')),
                ('name_of_user', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
