from django.utils import simplejson as json
from django import template

register = template.Library()


@register.filter
def encode_list(strng):
    return json.dumps(strng.split(','))
