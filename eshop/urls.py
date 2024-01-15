"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from store.models import *
from store.views import *


urlpatterns = [
    path("admin/", admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('login/', YourLoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),

    path('subcategory/<pk>/', SubcategoryDetailView.as_view(), name='subcategory_detail'),
    path('product-list/<pk>/', ProductListView.as_view(), name="product_list"),
    path('product/<pk>/', ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

