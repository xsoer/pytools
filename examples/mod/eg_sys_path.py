import sys
import os


# 把当前文件所在目录加入path内
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
print(sys.path)
# print(os.environ)