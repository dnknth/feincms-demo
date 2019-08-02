from django import template
from ..models import Page

register = template.Library()

@register.simple_tag
def main_menu():
    "Query top-level pages"
    return Page.objects.with_tree_fields().filter(
        parent=None, is_active=True)
