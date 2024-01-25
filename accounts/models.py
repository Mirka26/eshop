# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models import OneToOneField, CASCADE, DateField, ImageField, CharField, TextField
#
#
# class Profile(models.Model):
#     user = OneToOneField(User, on_delete=CASCADE, default=None, null=True)
#     title = CharField(max_length=50, blank=True, null=True)
#     GENDER_CHOICES = [
#         ('M', 'Muž'),
#         ('F', 'Žena'),
#         ('O', 'Ostatní'),
#     ]
#     gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
#     avatar = ImageField(upload_to="avatars/", default='avatars/default_avatar.webp', null=True, blank=True)
#     birth_date = DateField(null=True, blank=True)
#     mobile_number = CharField(max_length=15, blank=True, null=True)
#     address = TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username