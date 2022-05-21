import threading

import time


def main():
    threads = [
        threading.Thread(target=count, args=('post', 2)),
        threading.Thread(target=count, args=('video', 4)),
        threading.Thread(target=count, args=('like', 6)),
        threading.Thread(target=count, args=('comment', 8)),
    ]
    

    [th.start() for th in threads]

    print('Waiting processing ...')
    print('-' * 70)

    [th.join() for th in threads]

    print('Finished')

def count(obj, num):
    for n in range(1, num + 1):
        print(f'{n} {obj}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
