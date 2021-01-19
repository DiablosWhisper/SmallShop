#region             -----External Imports-----
from colorfield.fields import ColorField
from django.db.models import (Model, ImageField, TextField,
PositiveIntegerField, CharField, ManyToManyField,
DateTimeField, ForeignKey, SlugField, CASCADE)
from django.utils import timezone
from typing import TypeVar
#endregion

#region             -----Internal Imports-----
from .utils import (render_related_images, render_hex_color,
reverse_related_url)
#endregion

#region                -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Product(Model):
    #region           -----Information-----
    title=CharField(max_length=100, null=False, blank=False)
    discount=PositiveIntegerField(null=True, blank=True)
    price=PositiveIntegerField(null=False, blank=False)
    description=TextField(max_length=255, blank=False)
    #endregion

    #region            -----Database-----
    slug=SlugField(max_length=50, unique=True, blank=True)
    created_at=DateTimeField(default=timezone.now)
    updated_at=DateTimeField(default=timezone.now)
    #endregion

    #region            -----Relation-----
    related=ManyToManyField("self", blank=True)
    sizes=ManyToManyField("Size", blank=False)
    color=ForeignKey("Color", blank=True,
    on_delete=CASCADE, null=True)
    #endregion

    #region         -----External Methods-----
    def photos(self)->Html:
        """@return related images"""
        return render_related_images(
        images=self.photo_set.all())
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return product title"""
        return f"{self.title} {self.color}"
    #endregion

class Photo(Model):
    #region           -----Information-----
    photo=ImageField(upload_to="images", null=False)
    #endregion

    #region            -----Relation-----
    product=ForeignKey("Product", blank=False, 
    on_delete=CASCADE, default=1)
    #endregion

    #region         -----External Methods-----
    def title(self)->Html:
        """
        Displays the title of the image and
        the link for image editing\n
        @return editing link
        """
        return reverse_related_url(
        title=str(self.product),
        app="core", id=self.pk,
        model="photo")
    #endregion
    
    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return image url"""
        return self.photo.url
    #endregion

class Color(Model):
    #region           -----Information-----
    color=ColorField(default="#FF0000", null=False)
    title=CharField(max_length=20, default="",
    null=False)
    #endregion

    #region         -----External Methods-----
    def hex_color(self)->Html:
        """@return hex color"""
        return render_hex_color(
        color=self.color)
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return color title"""
        return self.title
    #endregion

class Size(Model):
    #region           -----Information-----
    size=CharField(max_length=5, null=False)
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return size title"""
        return self.size
    #endregion