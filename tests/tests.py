import os

from django.test import TestCase

from shop_richproduct.models import RichProduct


class SimpleTestCase(TestCase):
    """
    Simple test cases that verifies basic model functionality.
    """

    def setUp(self):
        """
        Set up the test environment.
        """

        # enable debug mode
        os.environ["DEBUG"] = "True"

    def tearDown(self):
        """
        Tear down the test environment.
        """

        pass

    def test_crud(self):
        """
        Create, store, update, and delete a rich product.
        """

        # create a product
        product = RichProduct()
        product.name = "Test Product"
        product.slug = "test-product"
        product.description = "this is a test product"
        product.unit_price = 6.50
        product.active = True
        product.purchase_button_label = "Buy"

        # save it
        product.save()
        product = None

        # retrieve it
        product = RichProduct.objects.get(slug="test-product")

        # verify its properties
        self.assertEquals(product.name, "Test Product")
        self.assertEquals(product.slug, "test-product")
        self.assertEquals(product.description, "this is a test product")
        self.assertEquals(product.unit_price, 6.50)
        self.assertEquals(product.active, True)
        self.assertEquals(product.purchase_button_label, "Buy")

        # delete it
        product.delete()
        product = None
