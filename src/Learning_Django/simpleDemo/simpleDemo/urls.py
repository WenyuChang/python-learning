from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views.SimpleViews import root
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # Self-developped views
    url(r'^$', root),
)

# Self-developped simple views
urlpatterns += patterns('simpleDemo.views.SimpleViews', 
    url(r'^helloworld/$', 'helloworldView'),
    url(r'^syspath/$', 'showPythonPath'),
    url(r'^showdate/$', 'showDate'),
    url(r'^showurlnum/(.+)/$', 'dynamicUrls'),
    # Using Named Groups
    # (?P<name>pattern)
    # more example to see urls.py in app_1
    url(r'^simpletemplatedemo/(?P<urlname>.+)/$', 'simpleTemplateDemo'),
    url(r'^templatedemo/$', 'templateDemo'),
    url(r'^showurlnumpassingtitle/(.+)/$', 'dynamicUrlsPassingExtraOptions', {'title': 'title passed from urls.py'}),
    # Please compared with dynamicUrlsPassingExtraOptions.
    # Since variable is named, the order of paremeters passed in method can be different
    url(r'^showurlnumpassingtitlenamed/(?P<num>.+)/$', 'dynamicUrlsPassingExtraOptionsNamed', {'title': 'title passed from urls.py'}),
)

# Self-developped views with templates
urlpatterns += patterns('simpleDemo.views.ViewsWithTemplates', 
    url(r'^template/showdate/', 'current_date'),
    url(r'^template/showdateshortcuts/', 'current_date_shortcuts'),
    url(r'^template/showdatelocals/', 'current_date_locals'),
    url(r'^template/showdateinclude/', 'current_date_include'),
    url(r'^template/showdateinherit/', 'current_date_inherit'),
    url(r'^template/templateescaping/', 'template_escaping'),
)

# Self-developped views from app_1
urlpatterns += patterns('', 
    url(r'^app_1/', include('app_1.urls')),
)