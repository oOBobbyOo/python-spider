from threading import Thread
from multiprocessing import Process


def func(name):
    for i in range(10):
        print(f'{name} {i}')


if __name__ == '__main__':
    # 创建线程
    # t1 = Thread(target=func, args=('周杰伦,'))
    # t2 = Thread(target=func, args=('周润发,'))
    # t3 = Thread(target=func, args=('周星驰,'))

    # t1.start()
    # t2.start()
    # t3.start()

    # 创建进程
    p1 = Process(target=func, args=('周杰伦,'))
    p2 = Process(target=func, args=('周润发,'))
    p3 = Process(target=func, args=('周星驰,'))

    p1.start()
    p2.start()
    p3.start()

    print('主线程')
