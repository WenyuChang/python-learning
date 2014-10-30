__author__ = 'wenychan'


class TimeLimitExpired(Exception): pass

def watch_dog1(func):
    def wrapped(*args, **kwargs):
        if 'timeout' in kwargs and kwargs['timeout'] > 0:
            timeout = kwargs['timeout']
            print '#'*10, timeout
            from multiprocessing import Process, Queue
            queue = Queue()
            kwargs['out_queue'] = queue
            process = Process(target=func, args=args, kwargs=kwargs)
            process.daemon = True
            process.start()
            process.join(timeout)
            if process.is_alive():
                process.terminate()
                raise TimeLimitExpired('#'*30)
            else:
                return queue.get()
    return wrapped

def watch_dog(func):
    def wrapped(*args, **kwargs):
        if 'timeout' in kwargs and kwargs['timeout'] > 0:
            timeout = kwargs['timeout']
            print '#'*10, timeout
            from threading import Thread
            class FuncThread(Thread):
                def __init__(self):
                    Thread.__init__(self)
                    self.result = None

                def run(self):
                    self.result = func(*args, **kwargs)

                def stop(self):
                    if self.isAlive():
                        Thread._Thread__stop(self)

            ft = FuncThread()
            ft.start()
            ft.join(timeout)
            if ft.isAlive():
                ft.stop()
                raise TimeLimitExpired('#'*30)
            else:
                return ft.result
        else:
            return func(*args, **kwargs)
    return wrapped