import sys

print(sys.version)

print(sys.api_version)

# 获取当前python版本
print(sys.version_info)

# 获取系统运行平台
print(sys.platform)

# 获取运行时参数
print(sys.argv)

# 获取sys.copyright
print(sys.copyright)

# 浮点信息
print(sys.float_info)

# 异常信息
print(sys.exc_info())


print(sys.getallocatedblocks())


# 当前编码信息
print(sys.getdefaultencoding())
# print(sys.getandroidapilevel())

# 系统编码信息
print(sys.getfilesystemencoding())

a = 1
print(sys.getrefcount(a))

# 获取递归限制
print(sys.getrecursionlimit())

# 线程信息
print(sys.thread_info)

# 堆栈信息打印
# print(sys.tracebacklimit())

# 运行退出
print(sys.exit(0)) # 正常退出。
print(sys.exit(1)) # 异常退出。非0皆为异常退出