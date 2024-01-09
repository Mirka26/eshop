from django.shortcuts import render

from store.models import *


# Create your views here.


def category(request):
    category_list = Category.objects.all()
    context = {'category': category_list}
    return render(request, 'category.html', context)


def parameter(request):
    parameter_list = Parameter.objects.all()
    context = {'parameter': parameter_list}
    return render(request, 'parameter.html', context)


def accessory(request):
    accessory_list = Accessory.objects.all()
    context = {'accessory': accessory_list}
    return render(request, 'accessory', context)






