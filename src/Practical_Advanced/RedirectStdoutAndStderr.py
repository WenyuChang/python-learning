__author__ = 'wenychan'

import sys
from StringIO import StringIO

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


if __name__ == '__main__':
    out = StringIO()
    err = StringIO()

    print('Fubar')

    with RedirectStdStreams(stdout=out, stderr=err):
        print("You'll never see me")

    print("I'm back!")

    print out.getvalue()
    print err.getvalue()