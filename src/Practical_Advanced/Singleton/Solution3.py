__author__ = 'wenychan'


class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance


class Singleton(object):
    __metaclass__ = SingletonType
    pass

if __name__ == '__main__':
    import SingletonTester
    SingletonTester.simple_test(Singleton)
    SingletonTester.multi_thread_test(Singleton)