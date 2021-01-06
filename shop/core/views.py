from django.shortcuts import render
from .models import Product

def catalog(request: object)->"HTML":
    """
    *Returns rendered HTML catalog page with products
    @param request: HTTP request
    @return rendered HTML page
    """
    for product in Product.objects.all():
        for related in product.related.all():
            print(related.color)
        print()
    return render(template_name="core/catalog.html",
    context={"products": Product.objects.all()},
    request=request)

def home(request: object)->"HTML":
    """
    *Returns rendered HTML home page
    @param request: HTTP request
    @return rendered HTML page
    """
    return render(request=request,
    template_name="core/home.html")