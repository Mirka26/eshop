from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import Form
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from store.models import *

from decimal import Decimal
from django.conf import settings




# Create your views here.
class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        images = Image.objects.all()
        categories = Category.objects.filter(parent_category=None)

        context = {
            "images": images,
            "categories": categories,
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

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        quantity = int(request.POST.get('quantity', 1))
        update_quantity = bool(request.POST.get('update_quantity'))

        cart_view = CartView()
        cart_view.add(product_id, quantity, update_quantity)

        # Redirect to cart or product detail page
        return HttpResponseRedirect(reverse('cart') or reverse('product_list', kwargs={'pk': product_id}))


class ProductDetailView(View):
    template_name = 'product_detail.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        context = {
            'product': product
        }
        return render(request, 'product_detail.html', context)

    # def post(self, request, *args, **kwargs):
    #     product_id = self.kwargs['pk']
    #     quantity = int(request.POST.get('quantity', 1))
    #     update_quantity = bool(request.POST.get('update_quantity'))
    #
    #     cart_view = CartView()
    #     cart_view.add(product_id, quantity, update_quantity)
    #
    #     # Redirect to cart or product detail page
    #     return HttpResponseRedirect(reverse('cart') or reverse('product-detail', kwargs={'pk': product_id}))




class YourLoginView(LoginView):
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

# class CartView(CreateView):
#     template_name = "cart.html"
#
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#     def add(self, product, quantity=1, update_quantity=False):
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
#
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#
#         self.save()
#
#     def remove(self, product):
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()
#
#     def save(self):
#         self.session.modified = True
#
#     def get_cart_contents(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)
#
#         cart = []
#         for product in products:
#             cart.append({
#                 'product': product,
#                 'quantity': self.cart[str(product.id)]['quantity'],
#                 'price': self.cart[str(product.id)]['price'],
#             })
#         return cart
#
#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

class CartView(TemplateView):
    template_name = "cart.html"

    def dispatch(self, request, *args, **kwargs):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)

    def add(self, product_id, quantity=1, update_quantity=False):
        # implementácia add metódy ako predtým...
        product = get_object_or_404(Product, id=product_id)
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()  # Opravené volanie metódy save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        quantity = int(request.POST.get('quantity', 1))
        update_quantity = bool(request.POST.get('update_quantity'))

        self.add(product_id, quantity, update_quantity)

        # Redirect to the cart page
        return HttpResponseRedirect(reverse('cart'))

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


