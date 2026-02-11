from django.test import TestCase
from product.factories import CategoryFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="food")

    def test_category_serializer(self):
        serializer = CategorySerializer(self.category)
        data = serializer.data

        self.assertEqual(data["title"], "food")
