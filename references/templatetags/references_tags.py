from django import template
from ..models import References
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.inclusion_tag('references/references/latest_references.html')
def show_latest_references(count=5):
    latest_references = References.published.order_by('-titleRf')[:count]
    return {'latest_references' : latest_references }


