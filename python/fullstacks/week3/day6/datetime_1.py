# @author: "QiuJunan"
# @date: 2018/3/17 11:47

# 关于datetime模块
import datetime
#获取年月日
print(datetime.date.today())
print(datetime.date.today().year)

#格式化日期
today = datetime.date.today()
today_format = today.strftime('%Y-%m-%d T %H:%M:%S')
print(today_format)