__author__ = 'wenychan'

# For version apscheduler 2.1.2

import time
import atexit
from apscheduler.scheduler import Scheduler


# Start the scheduler
sched = Scheduler(daemonic=True)
# register three exit handlers
atexit.register(lambda: sched.shutdown())
sched.start()

def job_function():
    print "Hello World"
    time.sleep(3)
    print "exit Hello World"

# Schedule job_function to be called every two hours
sched.add_interval_job(job_function, seconds=1, name='test_job1', max_instances=1)
sched.add_interval_job(job_function, seconds=3, name='test_job2', max_instances=1, max_runs=1) # sched.add_interval_job(job_function, seconds=5, name='test_job3', max_instances=1)
sched.add_interval_job(job_function, seconds=5, name='test_job3', max_instances=1)
sched.add_interval_job(job_function, seconds=6, name='test_job4', max_instances=1)
sched.add_interval_job(job_function, seconds=3, name='test_job5', max_instances=1)
sched.add_interval_job(job_function, seconds=1, name='test_job6', max_instances=1)
print len(sched.get_jobs())
time.sleep(5)
print len(sched.get_jobs())
time.sleep(50)