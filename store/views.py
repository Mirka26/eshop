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
            "products_in_category": products_in_category
        }
        return render(request, "subcategory_detail.html", context)

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        quantity = int(request.POST.get('quantity', 1))
        update_quantity = bool(request.POST.get('update_quantity'))

        cart_view = CartView()
        cart_view.add(product_id, quantity, update_quantity)

        # Redirect to cart or product detail page
        return HttpResponseRedirect(reverse('cart') or reverse('product_list', kwargs={'pk': product_id}))


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

        avg_rating = None
        if Rating.objects.filter(product=product).count() > 0:
            avg_rating = Rating.objects.filter(product=product).aggregate(Avg("rating"))

        user = request.user
        user_rating = None
        if request.user.is_authenticated:
            if Rating.objects.filter(product=product, user=user).count() > 0:
                user_rating = Rating.objects.filter(product=product, user=user)

        comments = Comment.objects.filter(product=product).order_by('-created')

        context = {
            'product': product,
            'avg_rating': avg_rating,
            'user_rating': user_rating,
            'comments': comments
        }
        return render(request, 'product_detail.html', context)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')


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
        product = get_object_or_404(Product, id=product_id)
        product_id = str(product.id)
        print("add_to_cart", product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "product_id": product_id,
                "name": product.name,
                'quantity': 0,
                'price': str(product.price),
                "total_price": 0}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['total_price'] = self.cart[product_id]['quantity'] * product.price
        else:
            self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['total_price'] = self.cart[product_id]['quantity'] * product.price

        self.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        total_price = 0
        for i in self.cart:
            print("item: ", i)
            print(self.cart)
            total_price += int(self.cart[i]['total_price'])
        context['total_price'] = total_price
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
        

def filter_by_price(request, min_price, max_price):
    filtered_products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'filtered_products': filtered_products,
        'selected_price_range': f'Od {min_price} do {max_price}',
    }

    return render(request, 'filtered_products.html', context)


def rate_product(request):
    user = request.user
    if request.method == 'POST':
        product_id = request.POST.get("product_id")
        product_obj = Product.objects.get(id=product_id)
        rating = request.POST.get("rating")

        if Rating.objects.filter(product=product_obj, user=user).count() > 0:
            user_rating = Rating.objects.get(product=product_obj, user=user)
            user_rating.rating = rating
            user_rating.save()
        else:
            Rating.objects.create(
                product=product_obj,
                user=user,
                rating=rating
            )
    return redirect(f"/product/{product_id}/")


def comment_product(request):
    user = request.user
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_obj = Product.objects.get(id=product_id)
        comment = request.POST.get('comment').strip()
        if comment:
            Comment.objects.create(
                product=product_obj,
                user=user,
                comment=comment
            )
    return redirect(f"/movie/{product_id}/")


def filter_by_rating(request, rating_type):
    if rating_type == 'popular':
        filtered_products = Product.objects.order_by('-rating')
    elif rating_type == 'less_popular':
        filtered_products = Product.objects.order_by('rating')
    else:
        filtered_products = Product.objects.all()

    context = {
        'filtered_products': filtered_products,
        'selected_rating_type': rating_type,
    }

    return render(request, 'filtered_products.html', context)


