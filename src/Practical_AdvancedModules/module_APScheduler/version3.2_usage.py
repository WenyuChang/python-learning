__author__ = 'Wenyu'

import logging, atexit, time
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig()
logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler(daemon=True)

def timed_job(aa, bb):
    logger.error("WenyuWenyuWenyu --- timed_job")
    logger.error(aa)
    logger.error(bb)
    print('This job is run every three minutes.')


def exit():
    logger.error("WenyuWenyuWenyu --- exit")
    scheduler.shutdown()
atexit.register(exit)
scheduler.start()

scheduler.add_job(timed_job,
                  'interval',
                  id='test_job',
                  name='metrics_sending',
                  seconds=3,
                  max_instances=1,
                  args=('aa', 'bb'),)

while True:
    time.sleep(1)

