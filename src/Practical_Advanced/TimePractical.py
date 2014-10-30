'''
Created on Feb 24, 2014

@author: wenychan
'''

def timeModule():
    import time
    print 'time.asctime(): ', time.asctime()
    # seconds after the epoch
    print 'time.asctime(time.gmtime(0)): ', time.asctime(time.gmtime(0))
    
    print 'time.localtime()', time.localtime()
    # year, month, mday, hour, minute, second, wday, yday, isdst = time.localtime()
    
    print 'time.strftime:', time.strftime("%a, %d %b %Y %H:%M:%S +0000")

if __name__ == '__main__':
    timeModule()