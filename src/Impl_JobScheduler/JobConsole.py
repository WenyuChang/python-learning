__author__ = 'wenychan'

from CommondParser import parse

if __name__ == '__main__':
    import sys
    while True:
        print 'jobs>',
        command = sys.stdin.readline()
        command = command.strip().lower()
        if len(command) == 0:
            continue

        args = parse(command)
        if args is not None:
            args.func(args)

        print