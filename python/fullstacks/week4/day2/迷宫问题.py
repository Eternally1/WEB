# @author: "QiuJunan"
# @date: 2018/3/28 10:24
# http://python.jobbole.com/87581/ 【参考链接】
# onenote中记载详细解题步骤
# 这里只会找到一条路径而不是所有的路径。
# 找出所有的路径，可以使用递归的方法

def initMaze():
    """初始化迷宫"""
    # 使用列表解析式创建一个7*7的二维数组
    maze =[[0]*7 for i in range(7)]
    # 将四周设置为1，表示墙壁，老鼠的移动只在内部的5*5内
    for i in range(7):
        maze[0][i] = maze[-1][i] = 1
        maze[i][0] = maze[i][-1] = 1
    # 记录墙的位置
    walls = [(1,3),(2,1),(3,3),(3,4),(4,2),(5,4)]
    for i,j in walls:
        maze[i][j] = 1
    return maze


def path(start, end, maze):
    """
    找从start到end的路径
    :param start: 起点坐标--元组
    :param end: 终点坐标--元组
    :param maze: 迷宫--二维数组
    :return:一个存储路径的栈
    """
    # 分解起始点和终止点的坐标
    i,j = start
    ei,ej = end
    stack = [(i,j)] # 将起点坐标存储起来
    maze[i][j] = 1  # 走过的位置置为1
    while stack:    # 当stack不为空的时候，接着走
        i,j = stack[-1] # 老鼠当前所在位置
        if (i,j) == (ei,ej):    # 表示找到终点了
            break
        for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
            if maze[i+di][j+dj] == 0:  # 表示可走的时候
                maze[i+di][j+dj] =1     # 将当前点置为1，表示走过
                stack.append((i+di,j+dj))   # 添加到栈中去
                break   # 跳出for循环，接着执行while循环
        else:   # 注意这里，在for循环里面if没有满足的时候，会执行这里的else语句
            stack.pop()     # 退回上一部[S]回溯？？
    return stack

def printMaze(maze):
    for i in range(len(maze)):
        print(maze[i],end='\n')

maze = initMaze()
stack = path((1,1),(5,5),maze)
print(stack)