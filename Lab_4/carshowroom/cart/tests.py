from django.test import TestCase, Client
from django.urls import reverse
from showroom.models import Category, Product
from .cart import Cart


class CartViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=10.0,
            stock=5
        )
        self.cart = Cart(self.client)
        self.cart.add(product=self.product)

    def test_cart_add_view(self):
        url = reverse('cart:cart_add', args=[self.product.id])
        response = self.client.post(url, data={'quantity': 1, 'update': False})
        self.assertEqual(response.status_code, 302)  # Redirects to cart_detail
        self.cart = Cart(self.client)  # Update the cart instance
        self.assertEqual(len(self.cart), 1)  # Existing item quantity + added quantity

    def test_cart_remove_view(self):
        url = reverse('cart:cart_remove', args=[self.product.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirects to cart_detail
        self.cart = Cart(self.client)  # Update the cart instance
        self.assertEqual(len(self.cart), 0)  # Item removed from the cart



    