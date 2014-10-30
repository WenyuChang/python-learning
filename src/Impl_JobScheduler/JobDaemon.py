__author__ = 'wenychan'

import atexit
import Pyro4
import importlib
from apscheduler.scheduler import Scheduler

class JobDaemon(object):
    def __init__(self):
        # Start the scheduler
        self.sched = Scheduler(daemonic=True)

        # register three exit handlers
        atexit.register(lambda: self.sched.shutdown())
        self.sched.start()

    def job_daemon_execute(self, module_name, func_name, *args, **kwargs):
        print 'Client request comming... ',
        print '[Module name:', module_name, '/',
        print 'Function name:', func_name, ']'
        command_module = importlib.import_module(module_name)
        func = getattr(command_module, func_name)
        result = func(sched=self.sched, *args, **kwargs)
        return result

job_daemon = JobDaemon()
pyro4_daemon = Pyro4.Daemon()
uri_file = open('uri.txt', 'w')
with uri_file:
    uri = str(pyro4_daemon.register(job_daemon))
    print uri
    uri_file.write(uri)
pyro4_daemon.requestLoop()
