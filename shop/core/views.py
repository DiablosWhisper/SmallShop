from django.shortcuts import render
from .models import Product

def home(request: object)->"HTML":
    return render(context={"products": Product.objects.all()},
    template_name="core/home.html", request=request)