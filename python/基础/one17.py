"""
编写一个不可以改变的自定义列表，要求记录列表中每个元素被访问的次数
"""

class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]

c1 = CountList(1,2,3,4,5)
c2 = CountList(2,3,4,5,6)

print(c1[1])
print(c2[1])
print(c1[1]+c2[1])
print(c1.count)
print(c2.count)
