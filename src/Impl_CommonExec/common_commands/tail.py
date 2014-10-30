__author__ = 'wenychan'

import sys
sys.path.append('..')

from Command import Command


def execute(executor, *args, **kwargs):
    tail_command = Command('tail -f')
    for arg in args:
        tail_command.add_argument(arg)

    tail = type(executor)(reference=executor)
    tail.add_command(tail_command)
    return tail()