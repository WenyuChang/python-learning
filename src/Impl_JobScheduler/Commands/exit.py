__author__ = 'wenychan'


def exit(args):
    import sys
    sys.exit()
# abbreviation

command = {}
command['name'] = 'exit'
command['help'] = "Exit the management console, same to command 'quit'"
command['func'] = exit