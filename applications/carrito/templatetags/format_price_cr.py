from django import template

register = template.Library()

@register.filter
def currency_format(value):
    return f'{value:,.0f} CLP'

@register.filter
def currency_format_with_symbol(value):
    return f'$ {value:,.0f} CLP'
