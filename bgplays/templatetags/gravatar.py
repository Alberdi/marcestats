import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ name|gravatar_url:150 }}
@register.filter
def gravatar_url(name, size=40):
    name += "@marcestats.com"
    name = name.encode('utf-8')
    return "https://www.gravatar.com/avatar/%s?%s" % (
    hashlib.md5(name).hexdigest(), urllib.parse.urlencode({'d': 'identicon', 's': str(size)}))

# return an image tag with the gravatar
# TEMPLATE USE:  {{ name|gravatar:150 }}
@register.filter
def gravatar(name, size=40):
    url = gravatar_url(name, size)
    return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))
