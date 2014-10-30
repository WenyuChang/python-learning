__author__ = 'wenychan'


class Singleton(object):
    __instance = None

    def __init__(self):
        self.var = 111

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

if __name__ == '__main__':
    import SingletonTester
    SingletonTester.simple_test(Singleton)
    SingletonTester.multi_thread_test(Singleton)
