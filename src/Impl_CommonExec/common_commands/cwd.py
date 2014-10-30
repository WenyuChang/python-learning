__author__ = 'wenychan'

import sys
sys.path.append('..')

from LocalExecutor import LocalExec
from RemoteExecutor import RemoteExec


def execute(executor, *args, **kwargs):
    if isinstance(executor, LocalExec):
        from plumbum import local
        context = local
    elif isinstance(executor, RemoteExec):
        context = executor.remote

    if len(args) == 0:
        print context.cwd
    elif len(args) == 1 and args[0].strip() != '':
        return context.cwd(args[0])


