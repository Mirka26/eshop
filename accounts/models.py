from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, CASCADE, DateField, ImageField, CharField, TextField


# Create your models here.


class Profile(User):
    user = User
    title = CharField(max_length=50, blank=True)
    GENDER_CHOICES = [
        ('M', 'Muž'),
        ('F', 'Žena'),
        ('O', 'Ostatní'),
    ]
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar = ImageField(upload_to="avatars/", default='avatars/default_avatar.webp')
    birth_date = DateField(null=True, blank=True)
    mobile_number = CharField(max_length=15, blank=True)
    address = TextField(blank=True)

    def __str__(self):
        return self.user.username
