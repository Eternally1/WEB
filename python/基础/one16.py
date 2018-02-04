"""
一个摄氏度  华氏度转换的例子
"""

class Celsius:
    def __init__(self,value=26.0):
        self.value = value
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value = value

class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel * 1.8 + 32
    def __set__(self,instance,value):
        instance.cel = (float(value)-32)/1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp = Temperature()
print(temp.cel)
temp.cel = 32
print(temp.cel,temp.fah)
temp.fah = 100
print(temp.cel,temp.fah)