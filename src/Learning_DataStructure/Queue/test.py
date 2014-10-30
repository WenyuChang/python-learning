__author__ = 'wenychan'

from Queue import Queue

queue = Queue(10)
queue.put(1)
queue.put(2)

print queue.qsize()

queue.get()
print queue.qsize()
queue.get()
print queue.qsize()