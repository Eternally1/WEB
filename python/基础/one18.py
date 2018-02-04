"""
用于one18-2.py的调用
"""
def c2f(cel):
    fah = cel*1.8+32
    return fah

def f2c(fah):
    cel = (fah-32)/1.8
    return cel

def foo():
    print("0摄氏度等于 %.2f华氏度" % c2f(0))
    print("0华氏度等于 %.2f摄氏度" % f2c(0))

#
if __name__ == '__main__':
    foo()
# print(__name__)

# 这里讲test改成对应的foo的时候，运行的时候就显示的是 Run one18，否者是
# Run unittests in one18.py,这种会出现错误，目前解决不了