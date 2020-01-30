from django import template
from django.utils.safestring import mark_safe

from minerals.models import Mineral


register = template.Library()


@register.filter('reverse_snake')
def reverse_snake(title):
    """Removes underscores in title and replaces them with a space."""
    return title.replace('_', ' ')
