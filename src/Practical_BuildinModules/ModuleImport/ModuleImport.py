__author__ = 'wenychan'


def simple_demo():
    from MyModule import fun
    fun()


def dynamic_import():
    module_name = 'MyModule'
    my_module = __import__(module_name)
    my_module.fun()

    another_module_name = 'module_package.MyAnotherModule'
    my_another_module = __import__(another_module_name, fromlist=['MyAnotherModule'])
    my_another_module.fun1()

    # print type
    module = __import__(another_module_name)
    module1 = __import__(another_module_name, fromlist=['MyAnotherModule'])
    print module
    print module1


def dynamic_with_importlib():
    import importlib

    module_name = 'MyModule'
    my_module = importlib.import_module(module_name)
    my_module.fun()

    another_module_name = 'module_package.MyAnotherModule'
    my_another_module = importlib.import_module(another_module_name, 'module_package')
    my_another_module.fun1()


if __name__ == '__main__':
    # __import__(module_name)
    # details seen KCSFullPull POC code
    # or use importlib.import_module()

    simple_demo()

    dynamic_import()

    dynamic_with_importlib()