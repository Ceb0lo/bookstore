from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from order.factories import OrderFactory


class TestOrderViewSet(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse",
            price=100,
            category=[self.category],
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product = response.data["results"][0]["product"][0]

        self.assertEqual(product["title"], self.product.title)
        self.assertEqual(product["price"], self.product.price)
        self.assertEqual(product["active"], self.product.active)

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            {"products_id": [product.id], "user": user.id},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
