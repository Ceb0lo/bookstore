from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product.factories import CategoryFactory


class TestCategoryViewSet(APITestCase):

    def setUp(self):
        self.category = CategoryFactory(title="books")

    def test_get_all_category(self):
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], self.category.title)

    def test_create_category(self):
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            {"title": "technology"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
