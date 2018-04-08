# @author: "QiuJunan"
# @date: 2018/3/20 9:26
# 将汉字转换成对应的数字
import re
CN_NUM = {
    '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
    '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2, '俩': 2
}
CN_UNIT = {
    '十': 10,
    '拾': 10,
    '百': 100,
    '佰': 100,
    '千': 1000,
    '仟': 1000,
    '万': 10000,
    '萬': 10000,
    '亿': 100000000,
    '億': 100000000,
    '兆': 1000000000000,
}
def c2a(cnumbers):
    """
    将中文汉字数字转换成对应的阿拉伯数字
    :param cnumbers: 含有汉字数字的字符串列表
    :return:
    """
    def _c2a(cn):
        """
        将如“两百万”转换成
        :param cn:
        :return:
        """
        unit = 0
        ldig = []
        for cndig in reversed(cn):
            # 将cn字符串倒置并遍历，变成[万,百,两]
            if cndig in CN_UNIT:
                unit = CN_UNIT.get(cndig)  #得到汉字数字对应的阿拉伯数字
                if unit == 100 or unit == 10000 or unit == 100000000:
                    ldig.append(unit)
                    unit = 1
            else:
                # “两”识别
                dig = CN_NUM.get(cndig)
                if unit:
                    dig *= unit
                    unit = 0
                ldig.append(dig)
        if unit == 10:
            ldig.append(10)
        val,tmp = 0,0
        for x in reversed(ldig):
            # 【S】有多个的时候，如10000,100时只处理一个就返回。
            if x == 100 or x == 10000 or x == 100000000:
                return x
            else:
                tmp += x
        val += tmp
        return val

    def _temp(string):
        """
        :param string:带有汉字数字的字符串
        :return:
        """
        if re.search(reg,string):  #扫描整个字符串并返回第一个成功的匹配
            if re.search('\d+[百千万亿]',string):  #如果存在这种形式，如10千，10百等
                # sub 这里的1表示只替换一次，也就是目前只用替换第一个匹配的结果
                # 注意观察这里的sub第一个参数[百千万亿]后面没有+号，此时表示只匹配数字后面的第一个汉字，之后循环递归匹配。
                r = re.sub('\d+[百千万亿]',str(int(re.search('\d+',string).group())*
                                          int(_c2a(re.search(reg,string).group()))),string,1)
            else:
                r = re.sub(reg,str(_c2a(re.search(reg,string).group())),string,1)
            # 循环的去依次转换对应的汉字数字成阿拉伯数字
            return _temp(r)
        else:
            return string

    # 从这里开始执行。
    result = []
    reg = re.compile('[零两俩一二三四五六七八九十百千万亿]+')   #匹配[]中数据一次或者多次
    for each in cnumbers:
        each = each.replace("左右","").replace("余","").replace("多","")   #去掉大概的修饰词
        trantab = str.maketrans('０１２３４５６７８９','0123456789')  #创建字符映射转换表
        each = each.translate(trantab)                     #用字符映射转换表进行字符串转换
        result.append(_temp(each))
    return result

if __name__ == '__main__':
    print(str.maketrans('０１２３４５６７８９', '0123456789'))
    s1 = ['死亡五百零一人受伤二十七人', '115人失踪十七人取得联系', '两人失踪', '１８００余人死', '两母女', '三天俩夜', '百人出席', '万人参赛', '20余万人', '3百万元美金']
    print(c2a(s1))

    # 可以根据一个具体的汉字数字进行过程的测试“3百万”