'''
Created on 2013.12.20

@author: wenychan
'''

from django import template

def setenv():
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'simpleDemo.settings'

def simpleDemo():
    t = template.Template('My name is {{ name }}.')
    c = template.Context({'name':'Wenyu Chang'})
    print t.render(c)

if __name__ == '__main__':
    setenv()
    simpleDemo()