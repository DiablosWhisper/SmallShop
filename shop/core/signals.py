from django.db.models.signals import (post_delete, 
m2m_changed, pre_save)
from .utils import generate_slug, get_related
from django.dispatch import receiver
from .models import Photo, Product

#region             -----Product Signals-----
@receiver(m2m_changed, sender=Product.related.through)
def pair_product(instance: object, sender: object, 
action: str, **kwargs)->None:
    #TODO: Implement auto-connection while association
        #* Function for collecting related objects
        #? Integrate algorithm into m2m_change
    pass

@receiver(pre_save, sender=Product)
def create_slug(instance: object,
sender: object, **kwargs)->None:
    """
    Generates unique slug using the title
    of the product and random postfix\n
    @return None
    """
    instance.slug=generate_slug(instance)
#endregion

#region              -----Photo Signals-----
@receiver(post_delete, sender=Photo)
def delete_on_delete(instance: object,
sender: object, **kwargs)->None:
    """
    Deletes file reference when the photo
    was removed from database\n
    @return None
    """
    instance.photo.delete(save=False)

@receiver(pre_save, sender=Photo)
def delete_on_change(instance: object,
sender: object, **kwargs)->None:
    """
    Deletes an old file the the photo
    was updated by user\n
    @return None
    """
    (Photo.objects.filter(pk=instance.pk).
    first().photo.delete(save=False) if
    instance.pk else "Do nothing")
#endregion