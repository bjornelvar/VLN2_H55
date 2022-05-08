import Levenshtein

from django import template

register = template.Library()

@register.filter(name='string_distance', is_safe=True)
def get_string_distance(string1, string2):
    string1_lower = string1.lower()
    string2_lower = string2.lower()
    return Levenshtein.distance(string1_lower, string2_lower)