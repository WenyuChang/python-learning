__author__ = 'wenychan'

import Pyro4


def daemon_list_scheduled_job(sched, *args, **kwargs):
    print 'Client request comming... list scheduled job.'
    if sched is not None:
        return sched.get_jobs()


def list_scheduled_job(args):
    uri_file = open('uri.txt', 'r')
    with uri_file:
        uri = uri_file.readline()

    proxy = Pyro4.Proxy(uri)
    jobs = proxy.job_daemon_execute(__name__, daemon_list_scheduled_job.__name__)
    if len(jobs) == 0:
        print 'No scheduled job...'
    else:
        for job in jobs:
            print job


command = {}
command['name'] = 'listscheduledjob'
command['help'] = 'List all scheduled Job instances'
command['func'] = list_scheduled_job