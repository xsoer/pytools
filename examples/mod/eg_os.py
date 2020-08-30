import os

# 打印系统名称
print(os.uname())

# 往环境变量里添加
os.environ.setdefault("key", "values")

# 打印环境
print(os.environ)

# 修改原来的环境变量
os.environ['ENV'] = 'value'

# 获取当前路径。到当前文件所在的文件夹
print(os.getcwd())
