from .models import Color, Size, Photo, Product
from django.contrib.admin import ModelAdmin
from django.contrib import admin

class ProductAdmin(ModelAdmin):
    exclude=("created_at", "updated_at", "slug")


admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Photo)
admin.site.register(Size)