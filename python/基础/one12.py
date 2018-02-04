origin = (0, 0)  # 原点
legal_x = [-10, 10]  # x轴上的合法范围
legal_y = [-50, 50]  # y轴上的合法范围


def create(pos_x=0, pos_y=0):
    def moving(direction, step):
    # direction规定执行的方向，有两个变量，第一个指示在x轴上移动的方向，第二个参数指示
    # y轴上的方向  1表示正方向  -1表示负方向  0表示不移动   step设置移动的距离
        nonlocal pos_x,pos_y
        new_x = pos_x+direction[0]*step
        new_y = pos_y+direction[1]*step
        #检查x轴是否越界
        if new_x<legal_x[0]:
        #当向左移动到边界之后就往右移动。
            pos_x = legal_x[0] - (new_x-legal_x[0])
        elif new_x>legal_x[1]:
            pos_x = legal_x[1] - (new_x-legal_x[1])
        else:
            pos_x = new_x
        # 检查y轴是否越界
        if new_y < legal_y[0]:
            pos_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y

        return pos_x,pos_y
    return moving

move = create()
print("向左移动11步后，位置是:",move([-1,0],11))
print("向上移动11步后，位置是:",move([0,1],11))