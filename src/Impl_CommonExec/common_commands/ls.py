__author__ = 'wenychan'

import sys
sys.path.append('..')

from Command import Command


def execute(executor, *args, **kwargs):
    ls_command = Command('ls')
    for arg in args:
        ls_command.add_argument(arg)

    ls = type(executor)(reference=executor)
    ls.add_command(ls_command)
    return ls()
