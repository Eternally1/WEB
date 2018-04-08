# @author: "QiuJunan"
# @date: 2018/3/31 12:08
import math

print("PI=",math.pi,"E=",math.e)
print(math.sin(2*math.pi/180))
print(math.sqrt(44))
print(math.pow(2,8))
print(abs(-3))
print(min(1,2,3,4),max(1,2,3,4),sum((1,2,3,4)))

# 关于去掉数值小数位的一些方法
print("*****去掉小数位的方法***********")
print(math.floor(2.3),math.floor(-2.3))
print(math.trunc(2.3),math.trunc(-2.6))
print(int(2.3),int(-2.6))
# round是四舍五入，但是需要超过5,第二个参数表示保存的小数的位数
print(round(2.4),round(2.51),round(-2.4),round(-2.51),round(2.5665,2))
# 格式化输出也会四舍五入
print("%.2f" % 2.336, "{0:.2f}".format(2.336))