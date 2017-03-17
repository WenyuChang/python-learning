__author__ = 'Wenyu'

from reporting.mailing import summary_init
import random
from multiprocessing import Process
import time

import logging
logging.basicConfig()

queue = summary_init()


def pq(reporting, id):
    for i in range(1300):
        if reporting:
            metric = 'metric' + id + str(i % 17)
            value = random.uniform(1, 1000)
            reporting.error('This is a error %s:%s' % (metric, value))
        time.sleep(0.1)


ps = []
for i in range(32):
    p = Process(target=pq, args=(queue, '-wenyu'))
    p.daemon = True
    ps.append(p)
    p.start()


for p in ps:
    p.join()