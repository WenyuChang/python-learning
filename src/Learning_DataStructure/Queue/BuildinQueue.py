__author__ = 'wenychan'





def producer_consumer_usage(produce_count=5, consumer_count=10):
    """Using build-in queue module as a blocking queue to demo producer and consumer problem"""

    import threading
    import time
    from Queue import Queue

    lock = threading.Lock()
    max_queue_size = 10
    product_queue = Queue(max_queue_size)

    class Product:
        def __init__(self, name):
            self.__name = name
            print '{0} is produced...'.format(self.__name)

        def consume(self, consumer):
            print '({0}) is consumed by {1}...'.format(self.__name, consumer)

    class Producer(threading.Thread):
        def __init__(self, name, cost=2, count=2):
            threading.Thread.__init__(self)
            self.__name = name
            self.__cost = cost
            self.__count = count

        def run(self):
            round_counter = 0
            while True:
                round_counter += 1
                for i in range(self.__count):
                    product_name = '{0}, {1}, {2}'.format(self.__name, str(round_counter), str(i))
                    try:
                        product_queue.put(Product(product_name), True, 2000)
                    except Queue.Full as e:
                        print 'Queue is full when produce products...'
                        print e
                time.sleep(self.__cost)

    class Consumer(threading.Thread):
        def __init__(self, name, cost=2):
            threading.Thread.__init__(self)
            self.__name = name
            self.__cost = cost

        def run(self):
            while True:
                lock.acquire()
                try:
                    product = product_queue.get(True, 2000)
                except Queue.Empty as e:
                    print 'Queue is empty when customer consume product...'
                    print e
                product.consume(self.__name)
                lock.release()

    for i in range(produce_count):
        producer = Producer('Producer '+str(i))
        producer.start()

    for i in range(consumer_count):
        consumer = Consumer('Consumer '+str(i))
        consumer.start()


if __name__ == '__main__':
    producer_consumer_usage()