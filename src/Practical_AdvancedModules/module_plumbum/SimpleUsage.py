'''
Created on Mar 26, 2014

@author: wenychan
'''

from plumbum import local, FG, BG


def basics_usage():
    ls = local["ls"]
    grep = local['grep']
    ls = chain = ls["-a"] | grep["-v", "\\.py"]
    ls()


def change_work_directory():
    # cwd = local.cwd
    # with local.cwd(path):
    #     ...
    pass

def piping():
    # ls = local['ls']
    # chain = li['-al'] | grep...
    # chain()
    pass

def redirection():
    # redir = ls >> ...
    # redir()
    pass

def FG_BG():
    # from plumbum import FG, BG
    # ls & FG
    # ls & BG
    pass

if __name__ == '__main__':
    basics_usage()
    pass