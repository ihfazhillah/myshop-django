# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180825_1424'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvailableProductManager',
        ),
    ]
