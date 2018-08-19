from django.test import TestCase
from .models import Product, ItemRequirements


class TestViews(TestCase):

    def test_get_product_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/products.html")
    