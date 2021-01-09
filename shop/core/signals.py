from django.db.models.signals import (post_delete, 
m2m_changed, pre_save)
from .utils import generate_slug, get_related
from django.dispatch import receiver
from .models import Photo, Product

@receiver(m2m_changed, sender=Product.related.through)
def pair_product(instance: object, sender: object, 
action: str, **kwargs)->None:
    """
    Associates the current product with
    all related products using BFS\n
    @return None
    """
    if action=="post_add":
        products=get_related(instance)
        for first in products:
            for second in products:
                if first!=second: first.related.add(second)

@receiver(post_delete, sender=Photo)
def delete_files(instance: object,
sender: object, **kwargs)->None:
    """
    Deletes file reference when the photo
    was removed from database\n
    @return None
    """
    instance.photo.delete(save=False)
    
@receiver(pre_save, sender=Product)
def create_slug(instance: object,
sender: object, **kwargs)->None:
    """
    Generates unique slug using the title
    of the product and random postfix\n
    @return None
    """
    instance.slug=generate_slug(instance)