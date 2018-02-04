# 简单定时器定制
"""
1、需要time模块的localtime方法来获取时间
2、time.localtime返回struct_time的时间格式
3、表现你的类：__str__  __repr__

这个代码还有许多不足，  可以查看课后作业中如何去完善。   第44节课


"""

import time as t
class MyTimer:
    def __init__(self):
        self.prompt = "未开始计时...."
        self.lasted = []  #定义一个列表，用来存放localtime间每个索引的差值
        self.begin = 0
        self.end = 0
        self.unit = ["年","月","日","小时","分钟","秒"]   #用于添加时间单位，显示的更加人性化

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：清先调用stop()停止计时"
        print("计时开始...")

    # 结束计时
    def stop(self):
        if not self.begin:
            print("提示：清先调用start()开始计时")
        else:
            self.end = t.localtime()
            print("计时结束...")
            self._calt()   #计算总共运行的时长。

    # 计算时长 内置方法
    def _calt(self):
        self.prompt = "总共运行了 "
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:   #非零的时候才会进来执行
                self.prompt += str(self.lasted[index]) + self.unit[index]

        #为下一轮初始化做准备
        self.begin = 0
        self.end  = 0

    def __add__(self, other):
        prompt = "总共运行了:"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    # 重写魔法方法
    def __str__(self):
        return self.prompt

    #这里可以不用再写一次 repr ，可以直接赋值
    __repr__ = __str__
