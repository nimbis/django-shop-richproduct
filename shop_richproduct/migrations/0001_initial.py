# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='RichProduct',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'rich_product')),
                ('description_placeholder', cms.models.fields.PlaceholderField(slotname=b'description_placeholder', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=('shop.product', models.Model),
        ),
    ]
