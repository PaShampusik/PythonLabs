from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Product


class CategoryModelTest(TestCase):
    def test_get_absolute_url(self):
        category = Category.objects.create(name="Test Category", slug="test-category")
        url = category.get_absolute_url()
        expected_url = reverse(
            "showroom:product_list_by_category", args=["test-category"]
        )
        self.assertEqual(url, expected_url)


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", slug="test-category"
        )
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            price=10.0,
            stock=5,
        )

    def test_get_absolute_url(self):
        url = self.product.get_absolute_url()
        expected_url = reverse(
            "showroom:product_detail", args=[self.product.id, self.product.slug]
        )
        self.assertEqual(url, expected_url)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_product_fields(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.slug, "test-product")
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.stock, 5)
        self.assertTrue(self.product.available)
        self.assertIsNotNone(self.product.created)
        self.assertIsNotNone(self.product.updated)


class ProductListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("showroom:product_list")
        self.category = Category.objects.create(
            name="Test Category", slug="test-category"
        )
        self.product1 = Product.objects.create(
            category=self.category,
            name="Product 1",
            slug="product-1",
            price=10.0,
            stock=5,
            available=True,
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name="Product 2",
            slug="product-2",
            price=15.0,
            stock=3,
            available=True,
        )

    def test_product_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "showroom/product/list.html")
        self.assertIn(self.product1, response.context["products"])
        self.assertIn(self.product2, response.context["products"])

    def test_product_list_view_by_category(self):
        category_url = reverse(
            "showroom:product_list_by_category", args=["test-category"]
        )
        response = self.client.get(category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "showroom/product/list.html")
        self.assertIn(self.product1, response.context["products"])
        self.assertIn(self.product2, response.context["products"])
