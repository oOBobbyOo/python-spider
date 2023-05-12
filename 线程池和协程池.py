from multiprocessing import Pool as ProressPool
from multiprocessing.dummy import Pool as ThreadPool
import time

start_time = time.time()


def get_pool(b_dump=True, num=4):
    """
    if b_dummy is True then get ThreadPool, or get process pool
    :param b_dummy: dummy thread Pool or Process pool
    :param num: thread or process num
    :return: pool object
    """

    if b_dump:
        pool = ThreadPool(num)
    else:
        pool = ProressPool(num)

    return pool


def get_page(str):
    print(f'正在下载： {str}')
    time.sleep(2)
    print(f'下载完成： {str}')


name_list = ['aa', 'bb', 'cc', 'dd']

# 实例化一个线程池对象, 子线程数为4
pool = get_pool()

# 将列表中的每个元素作为传递给get_page进行处理
pool.map(get_page, name_list)

end_time = time.time()

# 关闭子线程
pool.close()

# 关闭主线程
pool.join()

print('time consume %s' % (end_time - start_time))
