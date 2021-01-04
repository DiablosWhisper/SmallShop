from django.db.models import (Model, ImageField, TextField,
PositiveIntegerField, CharField, ManyToManyField, 
OneToOneField, DateTimeField, CASCADE)
from colorfield.fields import ColorField
from django.utils import timezone

class Photo(Model):
    #* Information region
    photo=ImageField(upload_to="images", null=False)
    
    #* Class inner methods
    def __str__(self)->str: return self.photo.name

class Color(Model):
    #* Information region
    color=ColorField(default="#FF0000", null=False)
    title=CharField(max_length=20, default="",
    null=False)

    #* Class inner methods
    def __str__(self)->str: return self.title

class Size(Model):
    #* Information region
    size=CharField(max_length=5, null=False)

    #* Class inner methods
    def __str__(self)->str: return self.size

class Product(Model):
    #* Information region
    title=CharField(max_length=100, null=False, blank=False)
    discount=PositiveIntegerField(null=True, blank=True)
    price=PositiveIntegerField(null=False, blank=False)
    description=TextField(max_length=255, null=False)

    #* Database region
    created_at=DateTimeField(default=timezone.now)
    update_at=DateTimeField(default=timezone.now)

    #* Relation region
    color=OneToOneField(Color, on_delete=CASCADE)
    related=ManyToManyField("self", blank=True)
    photos=ManyToManyField(Photo)
    sizes=ManyToManyField(Size)

    #* Class inner methods
    def __str__(self)->str:return self.title