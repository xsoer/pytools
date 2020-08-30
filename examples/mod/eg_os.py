import os

# 打印系统名称
print(os.uname())

# 往环境变量里添加
os.environ.setdefault("key", "values")

# 打印环境
print(os.environ)
