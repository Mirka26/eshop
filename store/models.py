from django.db import models
from django.db.models import Model, CharField, TextField, IntegerField
from django.contrib.auth.models import User


# Create your models here.
class Category(Model):
    name = CharField(max_length=64)


class Product(Model):
    name = CharField(max_length=32, null=False, blank=False)
    categories = CharField(max_length=32) #TODO: ManyToMany
    parameters = TextField()#TODO: ManyToMany
    description = TextField(null=True, blank=True)
    stock = TextField()
    availability = IntegerField()


class Cart(Model):
    pass


class Customer(Model):
    pass


class Order(Model):
    pass
