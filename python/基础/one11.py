# file_name =input("请输入要打开的文件名：")
# f = open(file_name)
#
# print("文件内容是：")
# for each_line in f:
#     print(each_line)
try:
    f = open("readme.txt")
    print(f.read())
    sum = 1 + '1'
# except OSError as err:
#     print("文件出错  错误的原因是:"+str(err))
# except TypeError as err:
#     print("类型出错   错误原因是:"+str(err))
#     不推荐下面这种
# except:
#     print("出错了")
except (OSError,TypeError):
    print("出错了")
finally:
    # finally里的语句一定会执行，用来表示哪怕文件后面的代码出错，仍然需要执行
    f.close()



