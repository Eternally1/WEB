# @author: "QiuJunan"
# @date: 2018/3/6 15:25
# 单线程执行
import time
def sorry():
    print("I Love You")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        sorry()