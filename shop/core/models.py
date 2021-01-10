from .utils import (render_related_images, render_hex_color)
from django.db.models import (Model, ImageField, TextField,
PositiveIntegerField, CharField, ManyToManyField,
DateTimeField, ForeignKey, SlugField, CASCADE)
from django.utils.html import format_html
from colorfield.fields import ColorField
from django.utils import timezone
from django.urls import reverse
from typing import List

#TODO: Create Cart model and etc.
#region                 -----Product Dependencies-----
class Product(Model):
    """Information region"""
    title=CharField(max_length=100, null=False, blank=False)
    discount=PositiveIntegerField(null=True, blank=True)
    price=PositiveIntegerField(null=False, blank=False)
    description=TextField(max_length=255, blank=False)

    """Database region"""
    slug=SlugField(max_length=50, unique=True, blank=True)
    created_at=DateTimeField(default=timezone.now)
    updated_at=DateTimeField(default=timezone.now)

    """Relation region"""
    related=ManyToManyField("self", blank=True)
    sizes=ManyToManyField("Size", blank=False)
    color=ForeignKey("Color", blank=True,
    on_delete=CASCADE, null=True)

    """Class outter methods"""
    def photos(self)->object:
        """@return related images"""
        return render_related_images(
        images=self.photo_set.all())

    """Class inner methods"""
    def __str__(self)->str:
        """@return product title"""
        return self.title

class Photo(Model):
    """Information region"""
    photo=ImageField(upload_to="images", null=False)
    product=ForeignKey("Product", blank=False, 
    on_delete=CASCADE, default=1)

    """Class outter methods"""
    @property
    def title(self)->object:
        """
        Displays the title of the image and
        the link for image editing\n
        @return editing link
        """
        link=reverse(args=[self.pk], 
        viewname=f"admin:core_photo_change")
        html=f"<a href='{link}'>image</a>"
        return format_html(html)
    
    """Class inner methods"""
    def __str__(self)->str:
        """@return image url"""
        return self.photo.url

class Color(Model):
    """Information region"""
    color=ColorField(default="#FF0000", null=False)
    title=CharField(max_length=20, default="",
    null=False)

    """Class outter methods"""
    def hex_color(self)->object:
        """@return hex color"""
        return render_hex_color(
        color=self.color)

    """Class inner methods"""
    def __str__(self)->str:
        """@return color title"""
        return self.title

class Size(Model):
    """Information region"""
    size=CharField(max_length=5, null=False)

    """Class inner methods"""
    def __str__(self)->str:
        """@return size title"""
        return self.size
#endregion

#region                  -----Cart Dependencies-----
#endregion