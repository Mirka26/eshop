from django.db import models
from django.db.models import Model, CharField, TextField, IntegerField, ManyToManyField, FloatField, ForeignKey, \
    DO_NOTHING, SET_NULL, DateTimeField, DateField, EmailField
from django.contrib.auth.models import User


# Create your models here.
class Category(Model):
    name = CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"


class Parameter(Model):
    name = CharField(max_length=64)


class Accessory(Model):
    name = CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Accessories"


class Product(Model):
    name = CharField(max_length=32, null=False, blank=False)
    price = FloatField()
    categories = ManyToManyField(Category, blank=True, related_name="product_category")
    parameters = ManyToManyField(Parameter, blank=True, related_name="product_parameter")
    accessories = ManyToManyField(Accessory, blank=True, related_name="product_accessory")
    stock = IntegerField()
    description = TextField(null=True, blank=True)


class Cart(Model):
    id_product = IntegerField()
    quantity = IntegerField()


class Customer(Model):
    first_name = CharField(max_length=32, null=False, blank=False)
    last_name = CharField(max_length=32, null=False, blank=False)
    birth_date = DateField(null=True, blank=True)
    address = TextField() # TODO: AddressField, spýtať sa
    email = EmailField(null=False, blank=False)
    mobile_number = CharField(max_length=16)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(Model):
    cart = ForeignKey(Cart, on_delete=DO_NOTHING)  # TODO : on_delete rozmyslieť sa
    order_date_time = DateTimeField()
    total_price = IntegerField() # TODO: FloatField?
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
    url = CharField(max_length=128, null=False, blank=False)

