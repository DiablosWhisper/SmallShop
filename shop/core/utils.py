from string import ascii_lowercase as letters
from django.utils.html import format_html
from django.utils.text import slugify
from string import digits
from typing import List
import random

#region             -----Render Functions-----
def render_related_images(images: List)->"HTML":
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

def render_hex_color(color: str)->"HTML":
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
#endregion

#region             -----Useful Functions-----
def get_related(instance: object)->List:
    """
    Finds all related product using iterative
    implementation of BFS algorithm\n
    @return related products
    """
    """Condition for adding node to sets"""
    go_to_next=(lambda node, queue, visited:
    not (node in queue or node in visited))

    """BFS iterative algorithm"""
    visited, queue={instance}, {instance}
    while queue:
        [(visited.add(node), queue.add(node))
        for node in queue.pop().related.all() 
        if go_to_next(node, queue, visited)]
    visited.remove(instance)
    return visited

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
#endregion