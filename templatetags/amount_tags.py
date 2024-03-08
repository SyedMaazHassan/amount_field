from django import template
from django.conf import settings

register = template.Library()

def format_currency(number=None):
    if not number:
        return 0

    number = float(number)

    # Format the number with commas and two decimal places
    formatted_text = "{:,.2f}".format(number)

    # Remove decimal if .00
    formatted_text = formatted_text.rstrip('0').rstrip('.')

    return formatted_text


@register.filter(name='amount_display')
def amount_display(value):
    price_unit = settings.AMOUNT_FIELD['price_unit']        
    return f"{price_unit} {format_currency(value)}"
