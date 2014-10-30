'''
Created on 2013.12.20

@author: wenychan
'''

from django.http import HttpResponse

title = '<title>Simple Demo Site Root Page</title>'

def helloworldView(request):
    html = '<html>%s<body><h1>This is my first Django view. </h1></body></html>' % (title, )
    return HttpResponse(html)

def root(request):
    html = '<html>%s<body><h1>%s</h1></body></html>'%(title, 'This is the root page of simple demo',)
    return HttpResponse(html)

def showPythonPath(request):
    import sys
    syspath = sys.path
    html = '<html>%s<body>%s</body></html>'%(title, syspath,)
    return HttpResponse(html)

def showDate(request):
    import datetime
    now = datetime.datetime.now()
    html = '<html><title>Simple Demo Website</title><body><h1>%s</h1></body></html>' % (now,)
    return HttpResponse(html)

def dynamicUrls(request, num):
    # personal design: if num is bigger than 100, it will return 404 error
    from django.http import Http404
    try:
        intnum = int(num)
        if intnum > 100:
            raise Http404()
    except:
        raise Http404()
    
    html = '<html>' + title + '<body><h1>' + num + '</h1></body></html>'
    return HttpResponse(html)

def simpleTemplateDemo(request, urlname): 
    from django import template
    t = template.Template('My name is {{ myname }}.')
    c = template.Context({'myname':urlname})
    returnStr = t.render(c)
    html = '<html>%s<body><h1>%s</h1></body></html>' % (title, returnStr, )
    return HttpResponse(html)

def templateDemo(request):
    from django import template
    # template can contain dictionary
    person = {'name':'wenychan', 'age':'26'}
    
    # template can contain object and method
    class Content:
        def get_content(self):
            print "Said: Hello world..."
            return "Hello world..."
    content = Content()

    templateStr = '{{ person.name }} is {{ person.age }} yesr(s) old. And he said {{ content.get_content }}'
    t = template.Template(templateStr)
    c = template.Context({'person':person})
    c['content'] = content
    returnStr = t.render(c)
    html = '<html>%s<body><h1>%s</h1></body></html>' % (title, returnStr, )
    return HttpResponse(html)

def dynamicUrlsPassingExtraOptions(request, num, title):
    # personal design: if num is bigger than 100, it will return 404 error   
    html = '<html><h1>' + title + '</h1><body><h1>' + num + '</h1></body></html>'
    return HttpResponse(html)

def dynamicUrlsPassingExtraOptionsNamed(request, title, num):
    # personal design: if num is bigger than 100, it will return 404 error   
    html = '<html><h1>' + title + '</h1><body><h1>' + num + '</h1></body></html>'
    return HttpResponse(html)