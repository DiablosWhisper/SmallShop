from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from .models import Photo, Product

@receiver(pre_delete, sender=Product)
def delete_references(sender: object, 
instance: object, **kwargs)->None:
    """
    Overrides default delete method\n
    @return None
    """
    instance.photos.all().delete()

@receiver(post_delete, sender=Photo)
def delete_on_delete(sender: object, 
instance: object, **kwargs)->None:
    """
    Overrides default delete method\n
    @return None
    """
    instance.photo.delete(save=False)