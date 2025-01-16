import threading
import time
from multiprocessing import Process, Queue

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"start: {i}")
        time.sleep(1)

def consumer(queue):
    while not queue.empty():
        item = queue.get()
        print(f"start: {item}")
        time.sleep(1)


if __name__ == "__main__":
    print("Main thread start.")

    thread = threading.Thread(target=print_numbers)
    thread.start()

    print("The main thread continues to run.")
    thread.join()
    print("main thread finish.")

    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

