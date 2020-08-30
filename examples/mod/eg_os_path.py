import os

print(__file__)

# 打印当前文件绝对路径
print(os.path.abspath(__file__))

# 打印文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))

# 创建文件夹。如果已经存在会报错
#os.mkdir('aa')

# 判断文件或文件夹是否存在
print(os.path.exists('aa'))