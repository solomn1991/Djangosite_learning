# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_test1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test1',
        ),
    ]
