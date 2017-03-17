__author__ = 'Wenyu'


from tornado.websocket import WebSocketHandler
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import logging
import os
import time
import json

from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG,
                    filename='ws_pq_cm.log',
                    filemode='w')
logger = logging.getLogger(__name__)

class WSApacheProxyHandler(WebSocketHandler):
    def check_origin(self, origin):
        return True


class PullHandler(WSApacheProxyHandler):
    def open(self):
        logger.info('CM[%s]: Got RGN Pull Connection.' % os.getpid())

    def on_message(self, message):
        logger.info('CM[%s]: Got RGN Pull Message. %s' % (os.getpid(), message))

        # Simulate message query for RGN side
        time.sleep(2)
        rec = ['rec1', 'rec2']

        logger.info('CM[%s]: Finish Message Query for RGN Side. ' % os.getpid())

        self.write_message(json.dumps({'success': True, 'messages': rec}))

    def on_close(self):
        logger.info('CM[%s]: Closed RGN Pull Connection.' % os.getpid())


class PushHandler(WSApacheProxyHandler):
    def open(self):
        logger.info('CM[%s]: Got RGN Push Connection.' % os.getpid())

    def on_message(self, message):
        logger.info('CM[%s]: Got RGN Push Message. %s' % (os.getpid(), message))

        # Simulate message persist at CM side
        time.sleep(2)

        logger.info('CM[%s]: Finish RGN Push Message Persist. ' % os.getpid())

        self.write_message(json.dumps({'success': True, 'retCode': 200}))

    def on_close(self):
        logger.info('CM[%s]: Closed RGN Push Connection.' % os.getpid())



application = tornado.web.Application([
    (r'/pull', PullHandler),
    (r'/push', PushHandler)
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    print '*** Websocket Server Started at %s***' % socket.gethostname()