from django import template
from blog.utils import rounded_time_ago  # Adjust the import path as needed

register = template.Library()

@register.filter
def rounded_time(value):
    return rounded_time_ago(value)
