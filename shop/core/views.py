#region             -----External Imports-----
from django.shortcuts import render
from typing import (Dict, TypeVar, List)
#endregion

#region             -----Internal Imports-----
from .services import ProductService
#endregion

def product(request: "Dict(HTTP|HTTPS)", slug: str)->"HTML":
    """
    Returns rendered HTML page with slug found product\n
    :param slug: slug to find product by\n
    :param request: dictionary\n
    @return rendered HTML page
    """
    product=ProductService().get_product_by(slug=slug)
    return render(template_name="core/product.html",
    context={"product": product}, request=request)

def catalog(request: "Dict(HTTP|HTTPS)")->"HTML":
    """
    Returns rendered HTML page with all found products\n
    :param request: dictionary\n
    @return rendered HTML page
    """
    products=ProductService().get_catalog_content()
    return render(template_name="core/catalog.html",
    context={"products": products},
    request=request)

def home(request: "Dict(HTTP|HTTPS)")->"HTML":
    """
    Returns rendered HTML page without context\n
    :param request: dictionary\n
    @return rendered HTML page
    """
    return render(request=request,
    template_name="core/home.html")