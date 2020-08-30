import threading
import time
from threading import Lock

# 不能够在lock里sleep,这样的话，是每个线程串行的sleep.

class T(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        a = 10
        try_times = 0
        while try_times < 5:
            try:
                with self.lock:
                    if a < 20:
                        print('sleeping...', try_times)
                        try_times += 1
                        time.sleep(10)
                        continue
                try_times = 0
                print('contintes')
            except Exception:
                try_times += 1
                continue
        print('over')


class T2(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        a = 10
        try_times = 0
        while try_times < 5:
            try:
                topic_id = None
                with self.lock:
                    if a < 20:
                        topic_id = 0
                if not topic_id:
                    print('sleeping...', try_times)
                    try_times += 1
                    time.sleep(10)
                    continue
                try_times = 0
                print('contintes')
            except Exception:
                try_times += 1
                continue
        print('over')


def t1():
    lock = Lock()
    for _ in range(2):
        t = T(lock)
        t.start()


def t2():
    lock = Lock()
    # 此处线程会串行执行
    for _ in range(2):
        t = T2(lock)
        t.start()
        t.join()


def t3():
    lock = Lock()
    t = []
    # 此处线程会并发执行
    for _ in range(2):
        t.append(T2(lock))
    for i in t:
        i.start()
    for i in t:
        i.join()


def t4():
    lock = Lock()
    t = []
    for _ in range(2):
        t.append(T(lock))
    for i in t:
        i.start()
    for i in t:
        i.join()


def main():
    start = time.time()
    # t1()
    # t2()
    # t3()
    t4()
    end = time.time()
    print('total-->', end - start)


if __name__ == "__main__":
    main()
