#region             -----External Imports-----
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from django.forms import ModelForm
#endregion

#region             -----Internal Imports-----
from .models import Color, Size, Photo, Product
#endregion

#region               -----Admin Forms-----
class ProductForm(ModelForm):
    """Class inner methods"""
    def __init__(self, *args, **kwargs)->None:
        """
        Excludes the current product from the list
        of many-to-many association products to
        prevent recursion call while saving\n
        @return None
        """
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["related"].queryset=(Product.objects.
        exclude(pk=self.instance.pk))

    """Class meta area"""
    class Meta: fields="__all__"; model=Product
#endregion

#region               -----Admin Pages-----
class ProductAdmin(ModelAdmin):
    fields=["title", ("price", "discount"), "description",
    ("related", "sizes", "color"), "photos"]
    list_display=["title", "price", "discount", "color"]
    list_filter=["title", "price", "discount", "color"]
    exclude=["created_at", "updated_at", "slug"]
    readonly_fields=["photos"]
    form=ProductForm

class ColorAdmin(ModelAdmin):
    list_display=["title", "hex_color"]

class PhotoAdmin(ModelAdmin):
    list_display=["title", "photo"]
#endregion

#region               -----Page Record-----
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size)
#endregion