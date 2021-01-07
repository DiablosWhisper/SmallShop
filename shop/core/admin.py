from .models import Color, Size, Photo, Product
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from django.contrib import admin

class ProductForm(ModelForm):
    """Class inner methods"""
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['related'].queryset=(Product.objects.
        exclude(pk=self.instance.pk))

    class Meta: 
        fields = "__all__"
        model=Product 
    
class ProductAdmin(ModelAdmin):
    exclude=["created_at", "updated_at", "slug"]
    form=ProductForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Color)
admin.site.register(Photo)
admin.site.register(Size)