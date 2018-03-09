#__author: "QiuJunan"
#date: 2018/2/24

#1、商品列表
#2、询问购买那个商品
#3、购买商品之后，这里就用已有的账户金额，减去购买的商品价格

products = [
    {
        "name":"Mac",
        "price":13200
    },
    {
        "name":"Book",
        "price":12
    },
    {
        "name":"bike",
        "price":500
    }
]

# 用于存储购买的商品
shoppingCar = []

def printProduct():
    print("\n*********商品列表如下***********")
    # 使用enumerate函数，可以在for循环中绑定索引
    for index, product in enumerate(products):
        # print(str((index+1))+'--'+"name:"+product["name"]+"  price:"+str(product["price"]))
        print("%d--name:%s  price:%d" % (index + 1, product["name"], product["price"]))


def buyProduct():
    global savingMoney
    global shoppingCar
    productIndex = input("请输入要购买的商品编号[退出:q]:")
    # 这里要判断输入的是否为数字
    if productIndex.isdigit():
        if (1 <= int(productIndex) <= len(products)):
            # print("有商品")
            # 判断是否可以购买
            # print(products[int(productIndex) - 1]["price"])
            product = products[int(productIndex) - 1]
            if (savingMoney >= product["price"]):
                shoppingCar.append(product)
                savingMoney = savingMoney-product["price"]
                print("购买" + product["name"] + "成功,还有" + str(savingMoney) + "RMB")
            else:
                print("你的余额为："+str(savingMoney)+"RMB,不够购买"+product["name"]+":"+str(product["price"]))
        else:
            print("不存在这个商品")
    # 判断何时退出
    elif productIndex in ["q","Q"]:
        print("谢谢购买，欢迎下次光临")
        return True
    else:
        print("请输入合法的指令")
    return False


# 先看存入的钱
while True:
    saving = input("please input your money:")
    if saving.isdigit():
        savingMoney = int(saving)
        # 每一次购买之后，都再次打印商品列表
        while True:
            printProduct()
            isQuit = buyProduct()
            if isQuit:
                break
        print("你购买的商品有:")
        # 添加属性，所购买商品的个数等信息，可以慢慢完善。
        print(shoppingCar)
        break
    else:
        print("请输入合法的金额")





