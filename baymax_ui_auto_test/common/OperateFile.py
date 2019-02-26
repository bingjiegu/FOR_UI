import os
import re

# 删除文件
def remove_file(f):
    if os.path.isfile(f):
        os.remove(f)
    else:
        print("%s文件不存在，无法删除" % f)


# 创建文件
def mkdir_file(f, method='w+'):
    if not os.path.isfile(f):
        with open(f, method, encoding="utf-8") as fs:
            print("创建文件%s成功" % f)
            pass
    else:
        print("%s文件已经存在，创建失败" % f)
        pass
#获取最新下载的文件夹的时间戳
def new_download_file_mtime():
    directory = "C:\\Users\\Administrator\\Downloads\\"
    if os.path.isfile(directory):
        pass
    else:
        print("%s文件不存在，无法删除" % directory)

    lists = os.listdir(directory)                                    #列出目录的下所有文件和文件夹保存到lists
    L = [i for i in lists if re.findall(r'(download_.*?\.zip)', i)]
    if not L:
        return False
    L.sort(key=lambda fn:os.path.getmtime(directory + "\\" + fn))  # 按时间排序
    file_new = os.path.join(directory,L[-1])                      # 获取最新的文件保存到file_new
    print('最新的文件为：',file_new)
    return os.path.getmtime(file_new)