import django.utils.html
from django.utils.safestring import SafeData

def safe_conditional_escape(html):
    #if isinstance(html, SafeData) or html.find('constraints') != -1:
    return html
    #else:
    #   return django.utils.html.escape(html)
    

django.utils.html.conditional_escape = safe_conditional_escape
