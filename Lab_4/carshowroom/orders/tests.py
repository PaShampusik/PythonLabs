# from django.test import TestCase
# from .models import Order, OrderItem
# from showroom.models import Product, Category
# from phonenumber_field.modelfields import PhoneNumberField

# class OrderModelTest(TestCase):
#     def setUp(self):
#         category = Category.objects.create(name='Test Category', slug='test-category')
#         self.order = Order.objects.create(
#             first_name='John',
#             last_name='Doe',
#             email='john@example.com',
#             number='+1234567890',
#             address='123 Main St',
#             postal_code='12345',
#             city='New York'
#         )
#         self.product = Product.objects.create(
#             category=category,
#             name='Test Product',
#             slug='test-product',
#             price=10.0,
#             stock=5
#         )
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             product=self.product,
#             price=10.0,
#             quantity=2
#         )

# class OrderItemModelTest(TestCase):
#     def setUp(self):
#         self.order = Order.objects.create(
#             first_name='John',
#             last_name='Doe',
#             email='john@example.com',
#             number='+1234567890',
#             address='123 Main St',
#             postal_code='12345',
#             city='New York'
#         )
#         self.product = Product.objects.create(
#             name='Test Product',
#             price=10.0,
#             stock=5
#         )
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             product=self.product,
#             price=10.0,
#             quantity=2
#         )

#     def test_order_item_fields(self):
#         self.assertEqual(self.order_item.order, self.order)
#         self.assertEqual(self.order_item.product, self.product)
#         self.assertEqual(self.order_item.price, 10.0)
#         self.assertEqual(self.order_item.quantity, 2)

#     def test_order_item_str(self):
#         self.assertEqual(str(self.order_item), str(self.order_item.id))

#     def test_get_cost(self):
#         cost = self.order_item.price * self.order_item.quantity
#         self.assertEqual(self.order_item.get_cost(), cost)