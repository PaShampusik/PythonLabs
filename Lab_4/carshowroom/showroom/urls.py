from django.urls import re_path, path
from . import views

urlpatterns = [
        path('', views.ProductListView.as_view(), name='product_list'),
        path('<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    re_path(r'^statistics', views.statistics, name ='statistics'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'), 
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),  
]