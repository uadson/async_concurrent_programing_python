import time
import colorama

from threading import Thread
from queue import Queue


def data_generator(queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f' Data {i} generated.', flush=True)
        time.sleep(2)
        queue.put(i)


def data_consumer(queue):
    while queue.qsize() > 0:
        value = queue.get()
        print(colorama.Fore.RED + f' Data {value * 2} processed.', flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'System Started', flush=True)
    queue = Queue()
    th1 = Thread(target=data_generator, args=(queue,))
    th2 = Thread(target=data_consumer, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()

    print(colorama.Fore.WHITE + 'Finished System', flush=True)
