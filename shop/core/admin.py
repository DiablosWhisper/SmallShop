from .models import Color, Size, Photo, Product
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from django.contrib import admin

class ProductForm(ModelForm):
    """Class inner methods"""
    def __init__(self, *args, **kwargs)->None:
        """
        1)Excludes the current product from the list
        of many-to-many association products to
        prevent recursion call while saving\n
        @return None
        """
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["related"].queryset=(Product.objects.
        exclude(pk=self.instance.pk))

    """Class meta area"""
    class Meta: fields="__all__"; model=Product
    
class ProductAdmin(ModelAdmin):
    fields=["title", ("price", "discount"), "description",
    ("related", "sizes", "color"), "photos"]
    exclude=["created_at", "updated_at", "slug"]
    readonly_fields=["photos"]
    form=ProductForm

class ColorAdmin(ModelAdmin):
    list_display=["title", "hex_color"]

class PhotoAdmin(ModelAdmin):
    list_display=["title", "photo"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size)