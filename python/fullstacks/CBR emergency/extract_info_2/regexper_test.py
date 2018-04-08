import re
def test1():
    shuzi = '一二三四五六七八九十百千万亿'
    中文数字='|'.join(shuzi)
    # pattern = re.compile("[\d{中文数字}\.\d{中文数字}]+")
    pattern = re.compile("(\d|{中文数字}|\.)+".format(中文数字=中文数字))
    print("(\d|{中文数字}|\.)+".format(中文数字=中文数字))
    print(pattern)
    print(中文数字)

def test2():
    # 注意这里
    pattern = re.compile("[\d]")
    print(pattern)
    ret = re.findall(pattern,"123ab345")
    print(ret)

def test3():
    trigger = ['经济损失', '损失', '过火面积', '直接损失', '扑火费用', '扑火', '农作物受灾面积', '牲畜', '麦田', '房屋',
               '森林面积', '折款', '桥梁受损', '损坏道路', '受灾面积', '受旱面积', '林木', '死亡大小牲畜', '桥梁', '重损', '轻损', '蔬菜大棚', '受灾人口',
               '民房', '小麦受灾面积', '电杆', '塌方', '房屋倒塌']
    shuzi = '一二三四五六七八九十百千万亿'
    loss_shu = ['十', '百', '千', '万', '十万', '百万', '千万', '亿', '十亿', '百亿', '千亿']
    liangci = ['元', '美元', '人民币', '间', '元钱', '亩', '座', '头', '户', '公里', '公顷', '立方米', '只', '个', '人', '平方米']
    ext = ['约', '左右', '已达', '多达', '至少', '达', '多', '近', '估计', '估计在', '余']

    # 受伤12人  倒塌房屋902间', 匹配1：'农作物受灾面积75.17千公顷，匹配2：民房受损844户2731间
    # ；直接经济损失近200万元
    # 我这里修改了一下，可以通过具体的例子测试一下。
    p1 = '|'.join([r'({触发词})+({ext})?(\d|{中文数字}|\.)+({ext})?({数})?({ext})?({单位量词})?'.format(触发词=each,
                                                                                  中文数字='|'.join(shuzi),
                                                                                  数='|'.join(loss_shu),
                                                                                  单位量词='|'.join(
                                                                                      liangci),
                                                                                  ext='|'.join(ext))
                   for each in trigger])

    pattern1 = re.compile(p1)
    pattern3 = re.compile(r'\d*[间户坐]?(房屋|桥梁)(不同程度)*(损坏|坍塌)')
    string = "直接损失700多公顷,经济损失达3000多万元"
    ret = re.finditer(pattern1,string)
    for i in ret:
        print(i.group())
    string2 = "256间房屋不同程度损坏，25户房屋坍塌"
    ret2 = re.finditer(pattern3,string2)
    for i in ret2:
        print(i.group())

# test1()
# test2()
test3()