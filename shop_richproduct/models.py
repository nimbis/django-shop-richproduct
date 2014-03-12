from django.db import models
from shop.models import Product
from cms.models.fields import PlaceholderField


class RichProductMixin(models.Model):
    '''
    A mixin for products that provides a description and image fields.
    '''

    description = models.CharField(max_length=255)
    description_placeholder = PlaceholderField('description_placeholder')
    image = models.ImageField(upload_to="rich_product")

    class Meta(object):
        abstract = True


class RichProduct(Product, RichProductMixin):
    '''
    A basic rich product.
    '''

    class Meta:
        pass
