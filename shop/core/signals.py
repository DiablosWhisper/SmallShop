#region             -----External Imports-----
from django.db.models.signals import (post_delete, 
m2m_changed, pre_save)
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .utils import generate_slug, get_related
from .models import Photo, Product
#endregion

#region             -----Product Signals-----
@receiver(m2m_changed, sender=Product.related.through)
def pair_product(instance: Product, action: str,
**kwargs)->None:
    #TODO: Implement auto-connection while association
        #* Function for collecting related objects
        #? Integrate algorithm into m2m_change
    pass

@receiver(pre_save, sender=Product)
def create_slug_on_create(instance: Product,
**kwargs)->None:
    """
    Generates unique slug using the title
    of the product and random postfix\n
    :param instance: product model\n
    @return None
    """
    instance.slug=generate_slug(instance)
#endregion

#region              -----Photo Signals-----
@receiver(post_delete, sender=Photo)
def delete_on_delete(instance: Photo,
**kwargs)->None:
    """
    Deletes file reference when the photo
    was removed from database by admin\n
    :param instance: photo instance\n
    @return None
    """
    instance.photo.delete(save=False)

@receiver(pre_save, sender=Photo)
def delete_on_change(instance: Photo,
**kwargs)->None:
    """
    Deletes an old file when the photo
    was updated by admin\n
    @return None
    """
    (Photo.objects.filter(pk=instance.pk).
    first().photo.delete(save=False) if
    instance.pk else "Do nothing")
#endregion