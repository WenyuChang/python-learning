myDic={'key1':'value1','key2':'value2',('1','2'):'value3'}
print("key1's value is %s" % myDic['key1'])
print("key2's value is %s" % myDic.get('key2'))
print("('1','2')'s value is %s" % myDic.get(('1','2')))

#============================================================
# Adding a key/value pair
myDic['key4'] = 'value4'
print('There are %d contacts in the myDic\n' % len(myDic))

#============================================================
# Deleting a key/value pair
del myDic['key2']
print('There are %d contacts in the myDic\n' % len(myDic))

#============================================================
# Show out the key value pair
for key, value in myDic.items():
    print('Contact %s at %s' % (key, value))

#============================================================
# if has some key
if 'key1' in myDic: 
    print("key1's value is %s" % myDic['key1'])

#============================================================
print('There are %d contacts in the myDic before popitem' % len(myDic))
myDic.popitem();
print('There are %d contacts in the myDic after popitem' % len(myDic))

#============================================================

print("dic.keys(): ", myDic.keys())
print("dic.values(): ", myDic.values())

#=============================================================

def func(fstr, **kwargs):
    print("func - fstr: ", fstr)
    print("func - *args:", kwargs)
    
func("test", arg1='arg1', arg2='arg2')