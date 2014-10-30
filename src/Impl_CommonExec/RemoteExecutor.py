__author__ = 'wenychan'

import sys
from Executor import AbsExecutor


class RemoteExec(AbsExecutor):
    def __init__(self, host='localhost', user=None, port=None, keyfile=None, password=None, command=None, reference=None):
        from plumbum import SshMachine
        super(RemoteExec, self).__init__(command)
        if reference is not None:
            self.__host = reference.host
            self.__user = reference.user
            self.__port = reference.port
            self.__keyfile = reference.keyfile
            self.__password = reference.password
            self.__remote = reference.remote
        else:
            self.__host = host
            self.__user = user
            self.__port = port
            self.__keyfile = keyfile
            self.__password = password
            if self.__password is not None:
                self.__remote = SshMachine(self.__host, self.__user, self.__port, password=self.__password)
            elif self.__keyfile is not None:
                self.__remote = SshMachine(self.__host, self.__user, self.__port, keyfile=self.__keyfile)
            else:
                self.__remote = SshMachine(self.__host, self.__user, self.__port)

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def port(self):
        return self.__port

    @property
    def keyfile(self):
        return self.__keyfile

    @property
    def password(self):
        return self.__password

    @property
    def remote(self):
        return self.__remote

    def _execute(self, command, bg=False, var=False, out=sys.stdout, err=sys.stderr):
        from plumbum import BG
        try:
            cmd = self.__remote[command.command]
            args = str(command).split(':')[1].strip().split(' ')
            return super(RemoteExec, self).execute(cmd, args, command, bg, var, out, err)
        except Exception as ex:
            print ex