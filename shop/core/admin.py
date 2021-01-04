from .models import Color, Size, Photo, Product
from django.contrib import admin

admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Photo)
admin.site.register(Size)