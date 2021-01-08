from django.db.models.signals import (post_delete, 
pre_delete, pre_save)
from django.dispatch import receiver
from .models import Photo, Product
from .utils import generate_slug

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
    instance.title+=(f" {instance.color}"
    if instance.color else "")