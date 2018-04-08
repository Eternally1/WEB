# @author: "QiuJunan"
# @date: 2018/3/17 20:49
# 修改threading1.py文件，使一下全部打印出来

import time
import threading
def sorry(name):
    print("I Love ",name)
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=sorry,args=("Tom",))
        t.start()

