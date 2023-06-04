from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from orders.models import Order, OrderItem
from django.views.generic import ListView
from django.db.models import Count, Sum
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from cart.forms import CartAddProductForm
import requests
import matplotlib.pyplot as plt

# def product_list(request, category_slug=None):
#     joke = get_random_joke()
#     rate = get_rate()
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
    
#     return render(request,
#                   'showroom/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products, 
#                    'joke' : joke,
#                    'rate': rate})

class ProductListView(ListView):
    model = Product
    template_name = 'showroom/product/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        sort = self.request.GET.get('sort')

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'name_asc':
            queryset = queryset.order_by('name')
        elif sort == 'name_desc':
            queryset = queryset.order_by('-name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_slug'] = self.kwargs.get('category_slug')
        context['categories'] = Category.objects.all()
        context['joke'] = get_random_joke()
        context['rate'] = get_rate()
        return context


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'showroom/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

def statistics(request):
    
    total_revenue = Order.objects.aggregate(total_revenue=Sum('items__price'))['total_revenue']

    # Получаем наиболее популярные машины (топ 5) и количество заказов для каждой из них
    popular_cars = OrderItem.objects.values('product__name').annotate(order_count=Count('product')).order_by('-order_count')[:5]
    car_labels = [car['product__name'] for car in popular_cars]
    order_counts = [car['order_count'] for car in popular_cars]
    # Создаем график для отображения популярности машин
    plt.bar(car_labels, order_counts)
    plt.xlabel('Машина')
    plt.ylabel('Количество заказов')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Сохраняем график во временном файле
    chart_path = 'media/graph.png'
    plt.savefig(chart_path)
    plt.close()
    # Передаем данные в шаблон и отображаем страницу статистики
    context = {
        'total_revenue': total_revenue,
    }
    return render(request, 'showroom/product/statistics.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock']
    success_url = reverse_lazy('showroom:product_list')  # Перенаправление после успешного обновления

    def form_valid(self, form):
        # Валидация цены
        price = form.cleaned_data.get('price')
        if price <= 0:
            form.add_error('price', 'Цена должна быть положительным числом.')

        # Валидация количества на складе
        stock = form.cleaned_data.get('stock')
        if stock < 0:
            form.add_error('stock', 'Количество на складе должно быть неотрицательным числом.')

        # Если есть ошибки валидации, возвращаем форму с ошибками
        if form.errors:
            return self.form_invalid(form)

        # Если валидация прошла успешно, сохраняем форму
        return super().form_valid(form)

# Представление для удаления продукта
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('showroom:product_list')  # Перенаправление после успешного удаления

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'stock']
    success_url = reverse_lazy('showroom:product_list')  # Перенаправление после успешного создания

    def form_valid(self, form):
        # Валидация цены
        price = form.cleaned_data.get('price')
        if price <= 0:
            form.add_error('price', 'Цена должна быть положительным числом.')

        # Валидация количества на складе
        stock = form.cleaned_data.get('stock')
        if stock < 0:
            form.add_error('stock', 'Количество на складе должно быть неотрицательным числом.')

        # Если есть ошибки валидации, возвращаем форму с ошибками
        if form.errors:
            return self.form_invalid(form)

        # Если валидация прошла успешно, сохраняем форму
        return super().form_valid(form)


def get_random_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    joke_data = response.json()
    joke = joke_data['setup'] + " " + joke_data['punchline']
    return joke

def get_rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    price_data = response.json()
    rate = "BitCoin/USD = " + price_data['bpi']['USD']['rate']
    return rate