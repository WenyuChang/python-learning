'''
Created on 2013.12.20

@author: wenychan
'''

from django import template
from django.http import HttpResponse
from django.template.loader import get_template

def current_date(request):
    import datetime
    now = datetime.datetime.now()
    t = get_template('template_learning/current_datetime.html')
    html = t.render(template.Context({'current_date': now}))
    return HttpResponse(html)

from django.shortcuts import render_to_response
def current_date_shortcuts(request):
    import datetime
    now = datetime.datetime.now()
    html = render_to_response('template_learning/current_datetime.html', {'current_date': now})
    return HttpResponse(html)

def current_date_locals(request):
    import datetime
    current_date = datetime.datetime.now()
    html = render_to_response('template_learning/current_datetime.html',  locals())
    return HttpResponse(html)

def current_date_include(request):
    import datetime
    current_date = datetime.datetime.now()
    name = 'Wenyu Chang'
    html = render_to_response('template_learning/include_demo/current_datetime.html',  locals())
    return HttpResponse(html)

def current_date_inherit(request):
    import datetime
    current_date = datetime.datetime.now()
    html = render_to_response('template_learning/inheritance_demo/inheritance_child.html',  locals())
    return HttpResponse(html)

def template_escaping(request):
    body_content = '<h1>This value is normal</h1><br />'
    body_content += "<script>alert('hello')</script>"
    
    body_content_off = '<h1>This value is abnormal. It will raise an alert. And make font bold</h1><br />'
    body_content_off += "<script>alert('hello')</script>"
    
    html = render_to_response('template_learning/advanced_demo/template_escaping.html',  locals())
    return HttpResponse(html)