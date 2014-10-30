from django.shortcuts import render
from django.http import HttpResponse

from models import Table1, Table2, Table3

# Create your views here.
def root(request):
    html = '<html><title>%s</title><body><h1>%s</h1></body></html>'%('App_1', 'This is the root page of App_1',)
    return HttpResponse(html)

def initDataToDB(request):
    try:
        t1 = Table1(field1_1='table1_field1', field2_1='www.test.com')
        t1.save()
            
        t2 = Table2(field1_2='table2_field1', field2_2='test@test.com')
        t2.save()
            
        import datetime
        t3 = Table3(field2_3=t1, field3_3=datetime.datetime.now())
        t3.save()
        t3.field1_3.add(t2)
    except:
        html = "Failed to insert one data to table1..."
    else:
        html = "Success to insert one data to table1..."
    finally:
        return HttpResponse(html)
    
def getDataFromTable(request, tableName):
    if tableName.lower() == 'table1':
        objects = Table1.objects.all().order_by("id")
    elif tableName.lower() == 'table2':
        objects = Table2.objects.all().order_by("id")
    elif tableName.lower() == 'table3':
        # Reversed order by id
        objects = Table3.objects.all().order_by("-id")
    else:
        from django.http import Http404
        raise Http404()
    
    html = 'Table: ' + tableName
    html += '<ol>'
    for obj in objects:
        html += '<li>%s</li>' % (obj, )
    html += '</ol>'
    
    return HttpResponse(html)

def getDataFromTableById(request, tableName, rowid):
    from django.http import Http404
    
    try:
        if tableName.lower() == 'table1':
            obj = Table1.objects.filter(id=rowid)[0]
        elif tableName.lower() == 'table2':
            # get method only get one row. 
            # If there are more than one row in DB, it will raise exception
            obj = Table2.objects.get(id=rowid)
        elif tableName.lower() == 'table3':
            obj = Table3.objects.get(id=rowid)
        else:
            raise Http404()
    except: 
        raise Http404()
    else:
        html = 'Table: ' + tableName
        html += '<ol>'
        html += '<li>%s</li>' % (obj, )
        html += '</ol>'
        
        return HttpResponse(html)

def updateDataFromTableById(request, tableName, rowid):
    from django.http import Http404
    
    try:
        if tableName.lower() == 'table1':
            # using save() will cause all the column being updated
            # no matter if other column has been changed 
            obj = Table1.objects.filter(id=rowid)[0]
            obj.field1_1 = 'table1_field1_updated'
            obj.field2_1 = 'www.test_updated.com'
            obj.save()
        elif tableName.lower() == 'table2':
            # if want only one column been changed
            # we can use update()
            obj = Table2.objects.filter(id=rowid)
            obj.update(field1_2 = 'table2_field1_updated')
            obj.update(field2_2 = 'test@test_updated.com')
            obj = obj[0]
        else:
            raise Http404()
    except: 
        raise Http404()
    else:
        html = 'Table: ' + tableName
        html += '<ol>'
        html += '<li>%s</li>' % (obj, )
        html += '</ol>'
        
        return HttpResponse(html)
    
def deleteDataFromTableById(request, tableName, rowid):
    from django.http import Http404
    
    try:
        if tableName.lower() == 'table1':
            # using save() will cause all the column being updated
            # no matter if other column has been changed 
            obj = Table1.objects.filter(id=rowid)[0]
            obj.delete()
        elif tableName.lower() == 'table2':
            # if want only one column been changed
            # we can use update()
            obj = Table2.objects.filter(id=rowid)
            obj.delete()
        else:
            raise Http404()
    except: 
        raise Http404()
    else:
        html = 'Success to delete data: ' + rowid + ' from table: ' + tableName
        return HttpResponse(html)

def getDataFromForm(request):
    from django.shortcuts import render_to_response
    return render_to_response('searchform.html')

def searchDataFromForm(request):
    if 'tablename' in request.GET and 'rowid' in request.GET:
        tableName = request.GET['tablename']
        rowid = request.GET['rowid']
        
        try:
            if tableName.lower() == 'table1':
                obj = Table1.objects.get(id=rowid)
            elif tableName.lower() == 'table2':
                obj = Table2.objects.get(id=rowid)
            elif tableName.lower() == 'table3':
                obj = Table3.objects.get(id=rowid)
            else:
                html = "<h1>No such Data</h1>"
                return HttpResponse(html)
        except: 
            html = "<h1>No such Data</h1>"
        else:
            html = 'Table: ' + tableName
            html += '<ol>'
            html += '<li>%s</li>' % (obj, )
            html += '</ol>'
            
            return HttpResponse(html)