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


def c2a(cnum):
    """替换语句中的中文数字为阿拉伯数字"""
    
    def _c2a(cn):
        unit = 0  # current
        ldig = []  # digest
        for cndig in reversed(cn):
            if cndig in CN_UNIT:
                unit = CN_UNIT.get(cndig)
                if unit == 100 or unit == 10000 or unit == 100000000:
                    ldig.append(unit)
                    unit = 1
            else:
                dig = CN_NUM.get(cndig)
                if unit:
                    dig *= unit
                    unit = 0
                ldig.append(dig)
        if unit == 10:
            ldig.append(10)
        val, tmp = 0, 0
        for x in reversed(ldig):
            if x == 100 or x == 10000 or x == 100000000:
                return x
            else:
                tmp += x
        val += tmp
        return val
    
    def _temp(strng):
        if re.search(reg, strng):
            # print(strng)
            # print(re.search('(\d+[百千万亿]+)', strng))
            if re.search('(\d+[百千万亿])', strng):
                r = re.sub('\d+[百千万亿]',
                           str(int(re.search('\d+', strng).group()) * int(_c2a(re.search(reg, strng).group()))),
                           strng, 1)
            else:
                r = re.sub(reg, str(_c2a(re.search(reg, strng).group())), strng, 1)
            return _temp(r)
        else:
            return strng
    
    reg = re.compile('[零两俩一二三四五六七八九十百千万亿]+')
    return [_temp(each.replace('左右', '').replace('余', '').replace('多', '')).translate(
        str.maketrans('０１２３４５６７８９', '0123456789')) for each in cnum]


if __name__ == '__main__':
    s1 = ['死亡五百零一人受伤二十七人', '115人失踪十七人取得联系', '两人失踪', '１８００余人死', '两母女', '三天俩夜', '百人出席', '万人参赛', '20余万人', '3百万元美金']
    print(c2a(s1))
