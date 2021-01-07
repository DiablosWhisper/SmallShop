from django.shortcuts import render
from .models import Product

def catalog(request: object)->"HTML":
    """
    Returns rendered HTML catalog page with products\n
    @param request: HTTP request\n
    @return rendered HTML page
    """
    return render(template_name="core/catalog.html",
    context={"products": Product.objects.all()},
    request=request)

def home(request: object)->"HTML":
    """
    Returns rendered HTML home page\n
    @param request: HTTP request\n
    @return rendered HTML page
    """
    return render(request=request,
    template_name="core/home.html")