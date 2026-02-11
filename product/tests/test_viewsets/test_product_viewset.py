from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = response.data["results"][0]

        self.assertEqual(product["title"], self.product.title)
        self.assertEqual(product["price"], self.product.price)
        self.assertEqual(product["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()

        data = {
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id],
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Product.objects.filter(title="notebook").exists())
