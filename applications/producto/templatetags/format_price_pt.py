from django import template
import locale

register = template.Library()

@register.filter
def format_price(value):
    locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')
    return locale.format_string('%d', value, True)
