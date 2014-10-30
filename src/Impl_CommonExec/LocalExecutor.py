__author__ = 'wenychan'

import sys
from Executor import AbsExecutor


class LocalExec(AbsExecutor):
    def __init__(self, command=None, reference=None):
        super(LocalExec, self).__init__(command)

    def _execute(self, command, bg=False, var=False, out=sys.stdout, err=sys.stderr):
        from plumbum import local, BG
        try:
            cmd = local[command.command]
            args = str(command).split(':')[1].strip().split(' ')
            return super(LocalExec, self).execute(cmd, args, command, bg, var, out, err)
        except Exception as ex:
            print ex


