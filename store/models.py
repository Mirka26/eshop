from django.db import models
from django.db.models import Model, CharField, TextField, IntegerField, ManyToManyField, FloatField, ForeignKey, \
    DO_NOTHING, SET_NULL, DateTimeField, DateField, EmailField, ImageField
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# from store.models import Product


# Create your models here.
class Accessory(Model):
    name = CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Accessories"


class Product(Model):
    name = CharField(max_length=128, null=False, blank=False)
    price = FloatField()
    categories = ManyToManyField("Category", blank=True, related_name="product_category")
    accessories = ManyToManyField(Accessory, blank=True, related_name="product_accessory")
    stock = IntegerField()
    brand = CharField(max_length=16)
    image = ManyToManyField("Image", null=True, blank=True, related_name="product_image")
    description = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Parameter(Model):
    name = CharField(max_length=64)
    value = CharField(max_length=64)
    id_product = ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Customer(Model):
    first_name = CharField(max_length=32, null=False, blank=False)
    last_name = CharField(max_length=32, null=False, blank=False)
    birth_date = DateField(null=True, blank=True)
    address = TextField()
    email = EmailField(null=False, blank=False)
    mobile_number = CharField(max_length=16)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cart(Model):
    id_product = ForeignKey(Product, on_delete=DO_NOTHING)
    customer = ForeignKey(Customer, on_delete=DO_NOTHING)
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    quantity = IntegerField()

    def __str__(self):
        return f"{self.name}"


class Order(Model):
    cart = ForeignKey(Cart, on_delete=SET_NULL, null=True)
    customer = ForeignKey(Customer, on_delete=DO_NOTHING)
    order_date_time = DateTimeField()
    total_price = FloatField()
    order_status = CharField(max_length=64)


class Rating(Model):
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    rating = IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.product} {self.rating} by {self.user}"


class Comment(Model):
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    comment = TextField(null=False, blank=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} {self.user}: {self.comment[:80]}"


class Image(Model):
    # url = CharField(max_length=128, null=False, blank=False)
    image = ResizedImageField(size=[400, 400], upload_to='static/images/', default=None, null=False, blank=False)  # , height_field=None, width_field=None, max_length=500)
    description = TextField()

    def __str__(self):
        return f"{self.description[:50]}"


class Category(Model):
    name = CharField(max_length=64)
    parent_category = ForeignKey("Category", on_delete=SET_NULL, null=True, blank=True, related_name="subcategories")
    # image = ForeignKey(Image, on_delete=SET_NULL, null=True, blank=True)
    image = ResizedImageField(size=[50, 50], upload_to='static/images')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class CartItem(Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"



