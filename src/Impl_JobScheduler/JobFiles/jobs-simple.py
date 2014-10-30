__author__ = 'wenychan'


def job_exec(*args, **kwargs):
    print 'Simple job executing...'
    print 'args: ', repr(args)
    print 'kwargs: ', kwargs