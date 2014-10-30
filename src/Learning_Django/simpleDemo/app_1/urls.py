'''
Created on 2013.12.20

@author: wenychan
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('app_1.views', 
    url(r'^$', 'root'),
    url(r'^initdata/$', 'initDataToDB'),
    url(r'^getdata/(table\d+)/$', 'getDataFromTable'),
    url(r'^getdatabyid/(table\d+)/(\d+)$', 'getDataFromTableById'),
    url(r'^updatedatabyid/(table\d+)/(\d+)$', 'updateDataFromTableById'),
    url(r'^deletedatabyid/(table\d+)/(\d+)$', 'deleteDataFromTableById'),
    # Using Named Groups
    # (?P<name>pattern)
    url(r'^getdatabyidnamed/(?P<rowid>\d+)/(?P<tableName>table\d+)/$', 'getDataFromTableById'),
    
    url(r'^getdatafromform/$', 'getDataFromForm'),
    url(r'^search/$', 'searchDataFromForm'),
)