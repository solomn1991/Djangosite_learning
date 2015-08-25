# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test1',
            field=models.CharField(default=1, max_length=200, verbose_name=b'test1'),
            preserve_default=False,
        ),
    ]
