__author__ = 'wenychan'


import datetime
import time
import atexit
from apscheduler.scheduler import Scheduler

def my_exit_hook_func(*args):
    print 'Shutdown scheduler...'
    sched.shutdown()
# register three exit handlers
atexit.register(my_exit_hook_func)


# Start the scheduler
sched = Scheduler(daemonic=True)
sched.start()
def my_job(text):
    print text
exec_date = datetime.datetime.now()
exec_date += datetime.timedelta(0,3)

# Store the job in a variable in case we want to cancel it
job = sched.add_date_job(my_job, exec_date, ['text'])

time.sleep(5)