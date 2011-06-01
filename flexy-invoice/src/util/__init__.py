import os
from google.appengine.ext.webapp import template

def render_template(handler, template_page = 'index.html', values = {}):
    path = os.path.join(os.path.dirname(__file__), '../templates/' + template_page)
    
    if not os.path.isfile(path):
        return False
    
    # Make a copy of the dictionary and add the path
    map = dict(values)
    map['path'] = handler.request.path
    
    html = template.render(path, map)
    handler.response.out.write(html)
    
    return True
    
