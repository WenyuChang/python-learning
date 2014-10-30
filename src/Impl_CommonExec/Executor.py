__author__ = 'wenychan'

from abc import ABCMeta, abstractmethod
from WatchDog import watch_dog, watch_dog1
from Command import Command
import sys


class AbsExecutor(object):
    __metaclass__ = ABCMeta

    def __init__(self, command=None):
        self._commands = {}
        self._command_order = []
        self.add_command(command)

    def add_command(self, command):
        self.insert_command_at(len(self), command)

    def insert_command_at(self, idx, command):
        if command is None:
            return

        if isinstance(command, str):
            if len(command.strip()) == 0:
                raise TypeError('Passin command type is not corrent.')
            command = Command(command)
            self._command_order.insert(idx, command.__hash__())
            self._commands[command.__hash__()] = command
        elif isinstance(command, Command):
            self._command_order.insert(idx, command.__hash__())
            self._commands[command.__hash__()] = command
        elif isinstance(command, list):
            for cmd in command:
                if isinstance(cmd, str):
                    cmd = Command(cmd)
                    self._command_order.insert(idx, cmd.__hash__())
                    self._commands[cmd.__hash__()] = cmd
                elif isinstance(cmd, Command):
                    self._command_order.insert(idx, cmd.__hash__())
                    self._commands[cmd.__hash__()] = cmd
                idx += 1
        else:
            raise TypeError('Passin command type is not corrent.')

    def show_commands(self):
        for i, hash in enumerate(self._command_order):
            print '[{0}]. {1}'.format(i, self._commands[hash])

    def remove_command(self, command):
        if command is None and not isinstance(command, Command):
            return

        hash = command.__hash__()
        if hash in self._commands:
            del self._commands

    def execute(self, cmd, args, command, bg=False, var=False, out=sys.stdout, err=sys.stderr):
        from plumbum import BG
        if var:
            if len(str(command).split(':')[1].strip()) > 0:
                retcode, retout, reterr = cmd[args].run()
            else:
                retcode, retout, reterr = cmd.run()
            return retcode, retout, reterr

        if bg:
            if len(str(command).split(':')[1].strip()) > 0:
                future = cmd[args] & BG
            else:
                future = cmd & BG
            return future
        else:
            if len(str(command).split(':')[1].strip()) > 0:
                if out is None and err is not None:
                    cmd[args](stderr=err)
                elif out is not None and err is None:
                    cmd[args](stdout=out)
                else:
                    cmd[args](stdout=out, stderr=err)
            else:
                if out is None and err is not None:
                    cmd(stderr=err)
                elif out is not None and err is None:
                    cmd(stdout=out)
                else:
                    cmd(stdout=out, stderr=err)
            return None

    @watch_dog
    def __call__(self, *args, **kwargs):
        if len(args) > 0 and len(self) == 1:
            command = self._commands[self._commands.keys()[0]]
            for arg in args:
                command.add_argument(arg)

        bg = kwargs.get('bg', False)
        var = kwargs.get('var', False)
        out = kwargs.get('out', sys.stdout)
        if type(out) is str:
            out = open(out, kwargs.get('write_type', 'a'))
        err = kwargs.get('err', sys.stderr)
        if type(err) is str:
            err = open(err, kwargs.get('write_type', 'a'))
        result = []
        for command in self._command_order:
            res = self._execute(self._commands[command], bg, var, out, err)
            if res is not None:
                result.append(res)
        if bg or var:
            if kwargs.get('out_queue', None) is not None:
                queue = kwargs.get('out_queue')
                queue.put(result)
            return result

    def __getitem__(self, args):
        if type(args) is slice:
            new_order_li = self._command_order[args]
            new_exec = type(self)()
            for i, hash in enumerate(new_order_li):
                new_exec.add_command(self._commands[new_order_li[i]])
            return new_exec

        if type(args) is str and len(args) > 0:
            command = args
            order = 1
        elif type(args) is tuple \
                and len(args) == 2 \
                and type(args[0]) is str \
                and type(args[1] is int):
            command = args[0]
            order = args[1]
            if order <= 0:
                order = 1
        else:
            raise NameError('No such command')

        cmd = None
        for value in self._commands.values():
            if command == value.command:
                cmd = value
                if order == 1:
                    break
                else:
                    order -= 1

        if cmd is not None:
            import copy
            new_command = copy.deepcopy(cmd)
            new_exec = type(self)(new_command)
            return new_exec
        else:
            return None

    def __len__(self):
        return len(self._command_order)

    def __getattr__(self, cmd):
        class CommandNotFound(LookupError): pass
        class ProxyCall(object):
            def __init__(self, executor, cmd):
                self.executor = executor
                self.cmd = cmd

            def __call__(self, *args, **kwargs):
                return self.cmd.execute(self.executor, *args, **kwargs)

        import common_commands
        from importlib import import_module
        common_cmds = common_commands.__all__
        if cmd not in common_cmds:
            raise CommandNotFound('Command %s no found' % cmd)

        cmd = import_module('common_commands.%s' % cmd)
        try:
            return ProxyCall(self, cmd)
        except Exception as ex:
            print ex

    def __add__(self, other):
        # self + other
        executor = type(self)()
        li, dict = (other._command_order, other._commands) + self
        executor._command_order = li
        executor._commands = dict
        return executor

    def __radd__(self, other):
        # other + self
        new_li = []
        new_dict = {}

        for value in other[0]:
            new_li.append(value)
        for value in self._command_order:
            new_li.append(value)

        for key, value in other[1].items():
            new_dict[key] = value
        for key, value in self._commands.items():
            new_dict[key] = value

        return new_li, new_dict

    # def __gt__(self, other):
    #     if type(other) is not tuple or len(other) > 2 or len(other) == 0:
    #         raise StandardError('Redirect Failure...')
    #
    #     if len(other) == 2:
    #         self(bg=False, out=other[0], err=other[1])
    #     else:
    #         self(bg=False, out=other[0], err=None)

    @abstractmethod
    def _execute(self, command): pass