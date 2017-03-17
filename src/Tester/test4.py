

from multiprocessing import Process

def enqueue(idx):
    for i in range(10):
        print i

if __name__ == '__main__':
    ps = []
    for i in range(1):
        p = Process(target=enqueue, args=(i, ))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()