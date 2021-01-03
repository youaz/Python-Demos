import gc
from memory_profiler import profile
from time import sleep


class A(object):
    def __init__(self):
        self.large_list = [i for i in range(1000000)]

    def trail(self):
        self.large_list = None
        print()

    def __del__(self):
        self.large_list = None
        print("__del__")


@profile
def foo():
    a = A()
    # a.trail()
    del a

    # gc.collect()
    sleep(1)
    print('over')


if __name__ == '__main__':
    print(gc.get_threshold())
    foo()

# 使用memory_profiler模块监控每行代码内存的变化
# python -m memory_profiler a.py
