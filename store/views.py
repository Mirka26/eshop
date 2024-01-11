from django.shortcuts import render

from store.models import *


# Create your views here.
def index(request):
    accessories = Accessory.objects.all()
    images = Image.objects.all()
    categories = Category.objects.all()
    context = {"accessories": accessories, "images": images, "categories": categories}
    return render(request, 'index.html', context)


# def categories(request):
#     categories_list = Category.objects.all()
#     context = {'categories', categories_list}
#     return render(request, 'categories.html', context)

# def category(request):
#     category_list = Category.objects.all()
#     context = {'category': category_list}
#     return render(request, 'category.html', context)
#
#
# def parameter(request):
#     parameter_list = Parameter.objects.all()
#     context = {'parameter': parameter_list}
#     return render(request, 'parameter.html', context)
#
#
# def accessory(request):
#     accessory_list = Accessory.objects.all()
#     context = {'accessory': accessory_list}
#     return render(request, 'accessory', context)
#
#

