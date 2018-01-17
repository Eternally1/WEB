user_data = {}

def new_user():
    prompt = "请输入用户名"
    while(True):
        username = input(prompt)
        if username in user_data:
            print("用户名已存在，请重新输入")
        else:
            break
    passwd = input("请输入密码:")
    user_data[username] = passwd
    print("用户已经注册")


def old_user():
    prompt = "请输入用户名:"
    while(True):
        username = input(prompt)
        if username not in user_data:
            print("你输入的用户名不存在，请重新输入")
        else:
            break
    passwd = input("请输入密码:")
    pwd = user_data.get(username)
    if passwd == pwd:
        print("欢迎进入系统")
    else:
        print("密码错误！")

# 显示菜单
def showmenu():
    prompt = """
    |---新建用户:N/n---|
    |---登录账号:E/e---|
    |---退出程序:Q/q---|
    |---请输入指令代码:
    """
    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)  # choice是字符串
            # 需要修正   输入Qq时也会执行else语句，但是指令应该是错误的.采用列表形式
            # if choice not in "NnQqEe":
            if choice not in ['Q','q','E','e','N','n']:
                print("输入的指令有误，请重新输入")
            else:
                chosen = True
        # 判断具体输入的字符
        if choice == "Q" or choice == "q":
            break
        if choice == "E" or choice == "e":
            old_user()
        if choice == "N" or choice == "n":
            new_user()
showmenu()


