from django.shortcuts import (render, get_object_or_404)
from .models import Product

def product(request: object, slug: str)->"HTML":
    """
    Returns rendered HTML page with slug found product\n
    @param request: HTTP request\n
    @return rendered HTML page
    """
    product=get_object_or_404(klass=Product, slug=slug)
    return render(template_name="core/product.html",
    context={"product": product}, request=request)

def catalog(request: object)->"HTML":
    #TODO: Beautify catalog method, reduce if-statements
    """
    Returns rendered HTML page with all found products\n
    @param request: HTTP request\n
    @return rendered HTML page
    """
    products=Product.objects.all()
    send, remove=set(), set()
    for product in products:
        if product not in remove: send.add(product)
        for related in product.related.all():
            if related not in remove and related not in send: remove.add(related)
    return render(template_name="core/catalog.html",
    context={"products": send},
    request=request)

def home(request: object)->"HTML":
    """
    Returns rendered HTML page without context\n
    @param request: HTTP request\n
    @return rendered HTML page
    """
    return render(request=request,
    template_name="core/home.html")