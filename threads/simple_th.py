import threading

import time


def main():
    th = threading.Thread(target=count, args=('post', 10))

    th.start()

    print('Waiting processing...')
    print('-' * 70)

    th.join()

    print('Finished')

def count(post, num):
    for n in range(1, num + 1):
        print(f'{n} {post}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
