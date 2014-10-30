__author__ = 'wenychan'

import hashlib


def md5_usage():
    md5 = hashlib.md5()
    md5.update("wenyu")
    md5.update("chang")
    print md5.digest()
    print md5.hexdigest()


def sha224_usage():
    sha224 = hashlib.sha224("wenyu chang")
    print sha224.digest()
    print sha224.hexdigest()


def other_algorithm_usage():
    print hashlib.algorithms
    h = hashlib.new('ripemd160')
    h.update('wenychan')
    print h.digest()


if __name__ == '__main__':
    md5_usage()

    print

    sha224_usage()

    print

    other_algorithm_usage()