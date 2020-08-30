import threading
import time
i = 0

def counter():
    global i
    i += 1
    print(i)


def print_test(n):
    for i in range(n):
        print(i)
        time.sleep(10)

if __name__ == "__main__":
    # for i in range(10):
        # threading.Thread(target=counter).start()
    a = threading.Thread(target=print_test, args=(10,))
    b = threading.Thread(target=print_test, args=(20,))

    a.start()
    b.start()

    a.join()
    b.join()