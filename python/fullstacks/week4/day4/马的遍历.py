# @author: "QiuJunan"
# @date: 2018/3/30 10:42

# 初始化马的8种走法
ways = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
row,col = 4,3
stack = [(0,0)] # 记录走过的路径，初始是从原点出发
path = [(0,0)]
a = [[0]*4 for i in range(5)]
a[0][0] = 1
count = 0

def mFind(x,y,dep):
    global count
    global a
    for ei,ej in ways:
        i = ei+x
        j = ej+y
        if check(i,j):
            a[i][j] = dep # dep可以表示什么时候访问到了i，j
            if dep == row*col:
                print(a)
                count += 1
            else:
                mFind(i,j,dep+1)
            a[i][j] = 0

def check(x,y):
    if x<0 or y<0 or x>=row or y>=col or a[x][y]!=0: # 不等于0表示已经访问
        return 0
    return 1

mFind(0,0,2)
print(count)

