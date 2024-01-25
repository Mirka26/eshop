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
from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.views import SignUpView, UserProfileView, EditProfileView, CreateProfileView
from store.models import *
from store.views import *
from store import views



urlpatterns = [
    path("admin/", admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('accounts/login/', LoginView.as_view(), name='login'),  # v djangu už to máme
    path('accounts/register/', SignUpView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # tieto cesty sú už defaultne v djangu

    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),

    path('subcategory/<pk>/', SubcategoryDetailView.as_view(), name='subcategory_detail'),
    path('product/<pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('add_to_cart/<int:product_id>/', CartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('remove/<pk>/', views.remove_from_cart, name='remove_from_cart'),

    path('rate_product/', rate_product, name='rate_product'),
    path('comment_product/', comment_product, name='comment_product'),

    path('filter_by_price/<int:min_price>/<int:max_price>/', filter_by_price, name='filter_by_price'),
    path('filter_by_rating/<str:rating_type>/', filter_by_rating, name='filter_by_rating'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

