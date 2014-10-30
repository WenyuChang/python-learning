__author__ = 'wenychan'

import sys


class FG(object):
    def __init__(self, **kwargs):
        self.out = kwargs.get('out', sys.stdout)
        self.err = kwargs.get('err', sys.stderr)
        self.timeout = kwargs.get('timeout', -1)
        self.write_type = 'w' if not kwargs.get('append', False) else 'a'

    def __rrshift__(self, cmd):
        return cmd(bg=False, out=self.out, err=self.err, timeout=self.timeout, write_type=self.write_type)


class BG(object):
    def __init__(self, **kwargs):
        self.out = None
        self.err = None
        self.timeout = kwargs.get('timeout', -1)

    def __rrshift__(self, cmd):
        return cmd(bg=True, out=None, err=None, timeout=self.timeout)


class VAR(object):
    def __init__(self, **kwargs):
        self.out = sys.stdout
        self.err = sys.stderr
        self.timeout = kwargs.get('timeout', -1)

    def __rrshift__(self, cmd):
        result = cmd(var=True, timeout=self.timeout)
        return result
