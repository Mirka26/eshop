from django.shortcuts import render

from store.models import *


# Create your views here.
def index(request):
    accessories = Accessory.objects.all()
    images = Image.objects.all()
    categories = Category.objects.all()
    context = {"accessories": accessories, "images": images, "categories": categories}
    return render(request, 'index.html', context)




