# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_richproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='richproduct',
            name='purchase_button_label',
            field=models.CharField(default=b'Purchase', help_text=b"The text that appears on this product's purchase button", max_length=64),
        ),
    ]
