__author__ = 'wenychan'

import Pyro4


def daemon_run_once(sched, *args, **kwargs):
    if 'job_name' in kwargs:
        print 'Client request comming... run job ({0}) once.'.format(kwargs['job_name'])
        # sched.add_interval_job(job_function, seconds=3, name='test_job2', max_instances=1, max_runs=1)
        return True
    else:
        print 'error'
        return False

def run_once(args):
    # Namespace(func=<function runonce at 0x0000000002EA0CF8>, job=['test'])
    if args.job is None or len(args.job) <= 0:
        return

    uri_file = open('uri.txt', 'r')
    with uri_file:
        uri = uri_file.readline()

    job_name = args.job[0]
    proxy = Pyro4.Proxy(uri)
    status = proxy.job_daemon_execute(__name__, daemon_run_once.__name__, job_name=job_name)
    print status

command = {}
command['name'] = 'runonce'
command['help'] = '''Schedule a Job to run once for now. This is similar to \"schedule -j xxx -id xxx -i xx -c 0\", the difference is that the job instance will be auto unscheduled after finish.'''
command['func'] = run_once
command['arguments'] = []

arg = {}
arg['name'] = '-j'
arg['full_name'] = '--job'
arg['help'] = 'specific the job name, which should be the same as job file name'
arg['metavar'] = 'job_name'
arg['nargs'] = 1
arg['required'] = True
command['arguments'].append(arg)