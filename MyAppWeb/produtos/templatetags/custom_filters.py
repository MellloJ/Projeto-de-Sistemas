from django import template

register = template.Library()

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='to_float')
def to_float(value):
    return float(value)