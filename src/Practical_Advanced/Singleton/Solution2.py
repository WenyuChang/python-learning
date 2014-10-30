__author__ = 'wenychan'

"""This code turns MyClass into a factory function, so you can't subclass it or use 'isinstance', etc."""


def singleton_decorator(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance


@singleton_decorator
class Singleton(object):
    pass

@singleton_decorator
class Singleton1(object):
    pass

if __name__ == '__main__':
    import SingletonTester
    SingletonTester.simple_test(Singleton)
    SingletonTester.multi_thread_test(Singleton)