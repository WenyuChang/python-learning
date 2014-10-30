__author__ = 'wenychan'


def quit(args):
    import sys
    sys.exit()
# abbreviation

command = {}
command['name'] = 'quit'
command['help'] = "Exit the management console, same to command 'exit'"
command['func'] = quit