#coding=UTF-8;
import random
secret  = random.randint(1,10);
# 设置机会次数
times = 2
print("...........猜数字游戏..........")
guess = 0;
print("猜数字开始:",end=" ");
while (secret!=guess) and (times>0):
    temp = input()
# 判断输入的是否为数字
    if(temp.isdigit()):
        guess = int(temp)
        if guess == secret:
            print("猜中了")
            break
        else:
            if guess>secret:
                print("大了")
            else:
                print("小了")
            if times>0:
                print("再试一次吧:",end=" ");
            else:
                print("机会用光了");
    else:
        print("你的输入有误，请输入数字:",end=" ");
    times -= 1;
print("游戏结束")
