from django.contrib import admin
from market.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'imageURL', 'stock', 'price', 'created', 'updated')

admin.site.register(Product)