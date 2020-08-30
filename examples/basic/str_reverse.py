"""
字符串逆序输出
"""
strs = input("输入字符串：")


def reverse0():
    new_str = ''
    for i in strs[::-1]:
        new_str += i
    print(new_str)


def reverse1():
    new_str = ''
    for i in range(len(strs) - 1, -1, -1):
        new_str += strs[i]
    print(new_str)


def reverse2():
    new_list = list()
    for i in range(len(strs)):
        new_list.append(strs[i])
    new_str = ''.join(reversed(new_list))
    print(new_str)


reverse0()
reverse1()
reverse2()
