__author__ = 'wenychan'

import glob
import os


job_file_path = 'C:\Users\wenychan\workspace\SELF-PROJECT\PythonLearning\src\AdvancedPractical\JobScheduler_Implementation\JobFiles'

def list_job(args):
    print 'jobs: '
    for job_file in glob.glob('{0}/jobs-*.py'.format(job_file_path)):
        print '  ', os.path.basename(job_file)

command = {}
command['name'] = 'listjob'
command['help'] = 'List all Job implementations in the hot folder'
command['func'] = list_job