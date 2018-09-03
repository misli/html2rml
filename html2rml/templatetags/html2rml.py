from django import template
from django.utils.safestring import mark_safe

from .. import html2rml as _html2rml

register = template.Library()


@register.filter
def html2rml(value):
    return mark_safe(_html2rml(value))
