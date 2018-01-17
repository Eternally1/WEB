
 def savefile(boy,kefu,count):
     file_name_boy = "boy_" + str(count) + ".txt"
     file_name_kefu = "kefu_" + str(count) + ".txt"

     # 打开文件
     boy_file = open(dirname + file_name_boy, "w")  # 以写入的形式打开
     kefu_file = open(dirname + file_name_kefu, 'w')

     # print(boy,kefu)
     # 写入文件
     boy_file.writelines(boy)
     kefu_file.writelines(kefu)

     boy_file.close()
     kefu_file.close()

# 打开文件
f = open("C:\\Users\\14259\Desktop\\temporary\\test.txt")
# 定义一下根目录
dirname = "C:\\Users\\14259\Desktop\\temporary\\"

# 然后使用两个列表分别存储分割之后的内容
boy = []
kefu = []

#需要一个count来给文件命名
count = 1

for each_line in f:
    if each_line[0:6] != "======":
        # print(each_line.split(":"))
        # print(each_line[:6])
        # 如果没有遇到分割符 ===，就直接分割程两部分,以冒号来分割
        (role,line_spoken) = each_line.split(":")
        if role == "小甲鱼":
            boy.append(line_spoken)
        if role == "小客服":
            kefu.append(line_spoken)
    else:
        # 分别命名文件
        savefile(boy,kefu,count)

        boy = []
        kefu = []
        count +=1
# 分别命名文件
savefile(boy,kefu,count)

f.close()

# 代码冗余，需要优化，使用函数
