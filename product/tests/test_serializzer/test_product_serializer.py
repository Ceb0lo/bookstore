from django.test import TestCase
from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100)
        self.product.category.add(self.category)  # se ManyToMany

    def test_product_serializer(self):
        serializer = ProductSerializer(self.product)
        data = serializer.data

        self.assertEqual(data["price"], 100)
        self.assertEqual(data["title"], "mouse")
        self.assertEqual(data["category"][0]["title"], "technology")