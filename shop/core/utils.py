from string import ascii_lowercase as letters
from django.utils.html import format_html
from django.utils.text import slugify
from string import digits
from typing import List
import random

def render_related_images(images: List)->str:
    """
    Generates and beautifies HTML code
    for displaying related images\n
    @return rendered HTML page
    """

    """Generates HTML and adds style to display"""
    html=[f"""<img src='{image}' style='height: 70px; 
    width: 70px'; display: inline-block;">"""
    for image in images]
    return format_html("\n".join(html))

def render_hex_color(color: str)->str:
    """
    Generates and beautifies HTML code
    for displaying hex color\n
    @return rendered HTML page
    """

    """Generates HTML and adds style to display"""
    html=f"""<a style='background-color: {color}; 
    display: inline-block; height: 20px; 
    width: 20px; border-radius: 50%;'>
    </a>"""
    return format_html(html)

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