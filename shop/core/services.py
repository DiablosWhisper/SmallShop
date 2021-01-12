#region             -----External Imports-----
from django.shortcuts import (get_object_or_404, get_list_or_404)
#endregion

#region             -----Internal Imports-----
from .models import Product
#endregion

#region             -----Product Service-----
class ProductService(object):
    #TODO: Refactor method
    def get_catalog_content(self)->"List[Product]":
        """
        Returns list of products to catalog page
        without duplicating related products\n
        @return list of products or raises 404
        """
        """Condition for hiding product"""
        hide_product=(lambda product, show, hide:
        not (product in hide or product in show))

        products=get_list_or_404(klass=Product)
        show, hide=set(), set()
        for product in products:
            if product not in hide: 
                show.add(product)
            [hide.add(related) 
            for related in product.related.all() 
            if hide_product(related, show, hide)]
        return show
        
    def get_product_by(self, **kwargs)->"Product":
        """
        Returns product by some user condition
        or if product isn't found raises 404\n
        @return product or raises 404
        """
        return get_object_or_404(klass=Product, **kwargs)
#endregion