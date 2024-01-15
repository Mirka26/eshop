from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views import View


from store.models import *


# Create your views here.
class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        images = Image.objects.all()
        categories = Category.objects.filter(parent_category=None)
        context = {
            "images": images,
            "categories": categories
        }
        return render(request, 'index.html', context)


class SubcategoryDetailView(View):
    template_name = "subcategory_detail.html"

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        subcategories = category.subcategories.all()
        products_in_category = Product.objects.filter(categories=category)

        context = {
            "category": category,
            "subcategories": subcategories,
            "products_in_category": products_in_category,
        }
        return render(request, "subcategory_detail.html", context)


class ProductListView(View):
    template_name = "product_list.html"

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        products_in_category = category.products.all()
        context = {
            'category': category,
            'products': products_in_category,
        }
        return render(request, 'product_list.html', context)


class ProductDetailView(View):
    template_name = 'product_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        context = {
            'product': product
        }
        return render(request, 'product_detail.html', context)





