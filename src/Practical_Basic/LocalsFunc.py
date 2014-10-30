'''
Created on 2013.12.20

@author: wenychan
'''

if __name__ == '__main__':
    var1 = 1
    var2 = '2'
    var3 = [3,4,5]
    var4 = {'key1':'val1', 'key2':'val2'}
    
    var_dic = locals()
    for key, value in var_dic.items():
        print '%s: %s' % (key, value)