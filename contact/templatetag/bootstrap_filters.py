# myapp/templatetags/bootstrap_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    """
    This filter adds a CSS class to a form field widget.
    """
    return value.as_widget(attrs={'class': css_class})
