# @author: "QiuJunan"
# @date: 2018/3/29 10:23
# 牛客网

# 何时算是成功逃出地牢？
# 到达地牢边界，也就是二维数组中去掉墙之后的边界
# 1、构建一个地牢，采用二维数组形式
# 2、求一个最大的步数，广度遍历
def init_maze(m,n):
    # [0]*n表示一个n个0的列表
    maze = [[0]*n for i in range(m)]
    # 设置墙壁
    for i in range(m):
        maze[i][0] = maze[i][-1] = 1
    for j in range(n):
        maze[0][j] = maze[-1][j] = 1

    # 设置障碍
    obstacle = [(2,3),(4,4)]
    for i,j in obstacle:
        maze[i][j] = 1
    # print(maze)
    return maze

# dep可以表示总共有多少个位置需要遍历
def mFind(x,y,dep,maze,number):
    for ei,ej in [(0,1),(0,-1),(-1,0),(1,0)]:
        xx = x+ei
        yy = y+ej
        if check(xx,yy,maze):
            maze[xx][yy] = dep
            if dep == number:
                print(maze)
            else:
                mFind(xx,yy,dep+1,maze,number)
            maze[xx][yy] = 0

def check(x,y,maze):
    # 这里注意一下 maze[x][y]的值要不为0才行，而不能是等于1，因为走过的点中，
    # 有很多都是赋值第几部走，而不是是否为1
    if x<0 or y<0 or x>=7 or y>=7 or maze[x][y] !=0:
        return 0
    return 1

def _get_point(maze):
    """获取maze中.的个数，也就是需要经过的地方"""
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0:
                count +=1
    return count

# # 2、先开始按照每次一步的方式来遍历
# def path(start,maze):
#     """传入开始的起点坐标，以及地牢"""
#     i,j = start
#     stack = [(i,j)]  #用来记录已经走过的路径
#     # 需要知道地牢maze中可以走的位置，不需要了
#     # count = _get_point(maze)
#     # print(count)
#     while stack:
#         i,j = stack[-1] # 每次循环需要更新i j的值
#         for ei,ej in [(-1,0),(0,1),(1,0),(0,-1)]:
#             # 如果可以走并且没有走过的时候
#             if maze[i+ei][j+ej] == '.' and (i+ei,j+ej) not in stack:
#                 stack.append((i+ei,j+ej))
#                 break
#         else:
#             stack.pop()


if __name__ == '__main__':
    maze = init_maze(5,6)
    number = _get_point(maze)
    maze[1][1] = 1
    mFind(1,1,2,maze,number)