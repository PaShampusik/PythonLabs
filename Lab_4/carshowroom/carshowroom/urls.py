"""
URL configuration for carshowroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static


urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path(r"^account/", include(("account.urls", "account"), namespace="account")),
    re_path(r"^cart/", include(("cart.urls", "cart"), namespace="cart")),
    re_path(r"^orders/", include(("orders.urls", "orders"), namespace="orders")),
    re_path(
        r"^information/",
        include(("information.urls", "information"), namespace="information"),
    ),
    re_path("", include(("showroom.urls", "showroom"), namespace="showroom")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
