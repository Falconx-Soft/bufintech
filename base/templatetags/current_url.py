
from django import template
import re
register = template.Library()

@register.filter
def current_url(value, url):
    url = url[4:]
    value = value.replace("_","-")
    if value == "analytic-apps":
        value = "analytical-applications"
    print(value, url)
    result = re.search(value , url)
    # print(value, type(value),url, type(url))
    if result != None:
        return True