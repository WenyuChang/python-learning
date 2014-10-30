__author__ = 'wenychan'

from jobargparse import RawTextHelpFormatter
import jobargparse as argparse
import copy


def help_func(args):
    print 'aaa'


def parse(command):
    command = command.split(' ')
    parser = parser_creatioin()
    args = parser.parse_known_args(command)
    if args is None:
        return args
    else:
        return args[0]


def parser_creatioin():
    parser = argparse.ArgumentParser(description='Job Scheduler Commands:', formatter_class=RawTextHelpFormatter, add_help=False)
    # parser.add_argument('-version', action='version', version='%(prog)s 1.0', help='Version of %(prog)s')
    subparsers = parser.add_subparsers(help='Sub-Command help')

    help_str = "Print usage and help info. To view help info of a command, use '<command> -h/--help'"
    parser_help = subparsers.add_parser('help', help=help_str)
    parser_help.set_defaults(func=parser.print_help_for_outside)

    # configure commands
    import Commands
    import importlib
    commands = Commands.__all__
    for command_module in commands:
        module_name = 'Commands.%s' % command_module
        command_module = importlib.import_module(module_name)
        if 'command' in dir(command_module):
            command = command_module.command
            parser_subcommand = subparsers.add_parser(command['name'], help=command['help'], formatter_class=RawTextHelpFormatter)
            parser_subcommand.set_defaults(func=command['func'])
            for commond_args in command.get('arguments', []):
                args = []
                kwargs = copy.copy(commond_args)
                args.append(commond_args['name'])
                del kwargs['name']
                if 'full_name' in commond_args:
                    args.append(commond_args['full_name'])
                    del kwargs['full_name']
                apply(parser_subcommand.add_argument, args, kwargs)
                #parser_subcommand.add_argument(arg_name, arg_full_name, help=arg_help, nargs='+', metavar='args')



    return parser