# @author: "QiuJunan"
# @date: 2018/3/17 21:06
# 通过线程类实现多线程
# 一般实际项目中也是这样来使用。

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg = "我是"+self.name
            print(msg)

if __name__ == '__main__':
    mythread = MyThread()
    # 会调用run方法。
    mythread.start()
    mythread1 = MyThread()
    mythread1.start()

