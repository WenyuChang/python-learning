__author__ = 'wenychan'


class Command(object):

    def __init__(self, command_line='', substitution=None):
        self.__arguments = []
        if substitution is None:
            self.__substitution = {}
        else:
            self.__substitution = substitution

        if command_line is None or len(command_line.strip()) <= 0:
            raise AttributeError('Command line can not be empty')

        command_line = command_line.strip()
        first_blank = command_line.find(' ')
        if first_blank > 0:
            self.__command = command_line[:first_blank]
            self.add_argument(command_line[first_blank:].strip())
        else:
            self.__command = command_line

    def add_argument(self, argument=''):
        argument = argument.strip()
        if argument is None or len(argument) <= 0:
            raise AttributeError('Command line can not be empty')

        args = argument.split(' ')
        for arg in args:
            self.__arguments.append(arg)

    def set_substitution_dict(self, dict=None, **kwargs):
        if dict is not None:
            for key, value in dict.items():
                self.__substitution[key] = value

        if kwargs is not None:
            for key, value in kwargs.items():
                self.__substitution[key] = value

    def __str__(self):
        command = self.__command + ': '
        args = ' '.join(self.__arguments)
        for key, value in self.__substitution.items():
            args = args.replace('${%s}' % key, value)

        command += args
        return command

    @property
    def command(self):
        return self.__command