from django.contrib import admin
from store.models import *
from django.contrib.admin import ModelAdmin


# Register your models here.
class ProductAdmin(ModelAdmin):

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id', 'name', 'brand']
    list_display = ['id', 'name', 'brand', 'price', 'stock']
    list_display_links = ['id', 'name', 'brand']
    list_per_page = 10
    list_filter = ['categories', 'brand']
    search_fields = ['name', 'brand']
    actions = ['cleanup_description']


admin.site.register(Category)
admin.site.register(Parameter)
admin.site.register(Accessory)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Image)
