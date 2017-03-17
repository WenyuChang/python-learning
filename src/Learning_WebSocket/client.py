__author__ = 'Wenyu'


import websocket
import thread
import time
import json
import logging

from multiprocessing import Process

HOST = 'ws://alln01-ats-cas9:8080'


def pqrgn_push():
    def cycle(ws):
        print 'Starting push cycle...'

        # Simulate Query Message for CM
        time.sleep(2)

        rec = ['rec3', 'rec4']
        print 'Starting Push Message %s to CM...' % rec
        ws.send(json.dumps(rec))
        print 'Finish Pushing Message %s to CM...' % rec

    def on_message(ws, message):
        print 'Got Response from CM Side. Response is %s' % message
        cycle(ws)

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "#Connection Closed..."

    def on_open(ws):
        cycle(ws)

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("%s/push/" % HOST,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def pqrgn_pull():
    def cycle(ws):
        print 'Starting pull cycle...'

        print 'Starting Pull Messages of Shard [%s - %s] from CM...' % (0, 7)
        ws.send(json.dumps(range(8)))

    def on_message(ws, message):
        print 'Got Response from CM Side. Response is %s' % message

        # Simulate Persisting message
        time.sleep(2)
        print 'Finish Persisting Message from CM Side'

        cycle(ws)

    def on_error(ws, error):
        print error

    def on_close(ws):
        print "#Connection Closed..."

    def on_open(ws):
        cycle(ws)

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("%s/pull/" % HOST,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == '__main__':

    push = Process(target=pqrgn_push, args=())
    push.daemon = True
    push.start()

    pull = Process(target=pqrgn_pull, args=())
    pull.daemon = True
    pull.start()

    while True:
        pass