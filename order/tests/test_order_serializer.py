from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self):
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        self.order = OrderFactory()
        self.order.product.add(self.product_1, self.product_2)

    def test_order_serializer(self):
        serializer = OrderSerializer(self.order)
        data = serializer.data

        self.assertEqual(data["product"][0]["title"], self.product_1.title)
        self.assertEqual(data["product"][1]["title"], self.product_2.title)
