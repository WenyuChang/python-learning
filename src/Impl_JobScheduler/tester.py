__author__ = 'wenychan'

import Pyro4
import datetime

file = open('uri.txt', 'r')
with file:
    uri = file.readline()
    print uri.strip()

proxy = Pyro4.Proxy(uri)
print proxy

def my_job():
    print 'text'
exec_date = datetime.datetime.now()
exec_date += datetime.timedelta(0,3)

# Store the job in a variable in case we want to cancel it
print proxy.schedule_job(my_job)

# import time
# time.sleep(5)