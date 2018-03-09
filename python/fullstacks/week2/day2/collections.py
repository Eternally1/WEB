# @author: "QiuJunan"
# @date: 2018/3/7 11:03

# collections  集合类
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
# point有什么作用？？
print("***************namedtuple****************")
Point = namedtuple('point',['x','y','z'])
p = Point(1,2,3)
print(p.x,p.y,p.z)
print(isinstance(p,tuple))


print("******************deque****************")
print("双向列表")
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)

print("************defaultdict***************")
print("不存在的key时，返回一个默认值")
dd = defaultdict(lambda:'不存在')
dd['k1'] = 'v1'
print(dd['k2'])

print("**************OrderedDict***************")
d = dict([('a',1),('b',2),('c',3)])
print(d)  #这里还是有序。可能是巧合
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)  #保证有序还是使用OrderedDict比较好

print("***************简单的计数器************")
c = Counter()
for ch in "programming":
    c[ch] = c[ch]+1
print(c)
