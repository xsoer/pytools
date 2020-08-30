import threading
import datetime


def t(a, b):
    print(a, b)
    for i in range(500):
        print('thread-'+str(a)+'=======>'+str(i))


thread1 = threading.Thread(target=t, args=(1, 3))
thread2 = threading.Thread(target=t, args=(2, 4))

start = datetime.datetime.now()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = datetime.datetime.now()

print('total time is :', end - start)
