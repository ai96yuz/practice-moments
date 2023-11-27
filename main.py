import threading

shared_resource = 0
lock = threading.Lock()


def modify_shared_resource():
    global shared_resource
    lock.acquire()
    try:
        for _ in range(1000000):
            shared_resource += 1
    finally:
        lock.release()
        pass


thread1 = threading.Thread(target=modify_shared_resource)
thread2 = threading.Thread(target=modify_shared_resource)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Значення спільного ресурсу:", shared_resource)
