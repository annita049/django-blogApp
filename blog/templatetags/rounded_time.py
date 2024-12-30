from django import template
from blog.utils import rounded_time_ago  # Adjust the import path as needed

register = template.Library()

@register.filter
def rounded_timesince(value):
    return rounded_time_ago(value)

@register.filter
def formatted_date(value):
    """
    This custom filter formats the date as '24 March, 2023'.
    """
    if not value:
        return value
    
    return value.strftime('%d %B, %Y')