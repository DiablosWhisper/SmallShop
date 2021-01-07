from string import ascii_lowercase as letters
from django.utils.text import slugify
from string import digits
import random

def generate_slug(instance: object, 
generated_slug: str=None)->str:
    """
    Generates unique slug using the title
    of the product and random postfix\n
    @return generated slug
    """
    """Generates slug using letters and digits"""
    generate=lambda slug: slug+"-"+"".join([
    random.choice(letters+digits) 
    for _ in range(7)])

    """Stop condition for recursion calling"""
    slug=(generated_slug if generated_slug
    else slugify(instance.title))

    """Searching for an existing slug"""
    exists=(type(instance).objects.
    filter(slug=slug).exists())

    return (generate_slug(instance=instance,
    generated_slug=generate(slug)) if exists
    else slug)