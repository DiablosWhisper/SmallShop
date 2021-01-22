#region             -----External Imports-----
from django.shortcuts import (get_object_or_404, get_list_or_404)
from typing import TypeVar, List
#endregion

#region             -----Internal Imports-----
from ..models import Product
#endregion

#region             -----Product Service-----
class ProductService(object):
    def get_product_by_any(self, **kwargs)->Product:
        """
        Returns product by some user condition
        or if product isn't found raises 404\n
        @return product or raises 404
        """
        return get_object_or_404(klass=Product, **kwargs)
        
    def get_catalog_content(self)->List[Product]:
        """
        Returns list of products to catalog page
        without duplicating related products\n
        @return list of products or raises 404
        """
        return Product.objects.distinct("title")
#endregion