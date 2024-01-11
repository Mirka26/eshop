from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from store.models import *


# Create your views here.
def index(request):
    accessories = Accessory.objects.all()
    images = Image.objects.all()
    categories = Category.objects.all()
    context = {"accessories": accessories, "images": images, 'categories': categories}
    return render(request, 'index.html', context)


# def products(request):
#     products_obj = Product.objects.all()
#     context = {"products": products_obj}
#     return render(request, "products.html", context)


def product_list(request):
    product_lists = Product.objects.all()

    # Nastavenie stránkovania
    paginator = Paginator(product_lists, 10)  # Zobrazí 10 produktov na stránku
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # Ak parameter 'page' nie je číslo, zobraz prvú stránku
        products = paginator.page(1)
    except EmptyPage:
        # Ak stránka neexistuje, zobraz poslednú stránku
        products = paginator.page(paginator.num_pages)

    return render(request, 'product_lists.html', {'products': products})



