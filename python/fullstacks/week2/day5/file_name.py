# @author: "QiuJunan"
# @date: 2018/3/9 8:38
# python获取目录列表信息
# 会自动根据是否为子目录来进行遍历递归。
"""
已经完成文件名的写入，接下来的任务是将所有pdf转换为txt文件。注意文件路径中双斜杠
"""
import os
# file_dir为要访问的目录文件，filename为最后文件保存的位置。
def file_name_list(file_dir,filename):
    #将文件清空,以w格式打开文件，如果文件存在，则清空，否则创建文件。
    with open(filename,'w') as f:
        pass;
    for root,dirs,files in os.walk(file_dir):
        # print("当前目录路径--",root)
        # print("子目录有--",dirs)
        # print("文件有--",files)
        #每一个files是一个列表，这里需要将名字改成完整形态
        for file in files:
            file_name = os.path.join(root,file)
            #写入到文件
            with open(filename, 'a') as f:
                f.write(file_name)
                f.write("\n")
    print("文件名已经写入到", filename, "文件中")
    # 返回文件保存的地址
    return filename

# file_name_list(path)
