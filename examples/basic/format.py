
# %% 位置
print("{0} {1}".format("hello", "world"))
print("{} {}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))

# %% 关键字
print("I am {name}, age is {age}".format(name="huoty", age=18))
user = {"name": "huoty", "age": 18}
"I am {name}, age is {age}".format(**user)


# %% 类处理
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{self.name}({self.age})".format(self=self)

    def __repr__(self):
        return self.__str__()


user = User("huoty", 18)
print(user)
"I am {user.name}, age is {user.age}".format(user=user)

# %% 通过下标
names, ages = ["huoty", "esenich", "anan"], [18, 16, 8]
"I am {0[0]}, age is {1[2]}".format(names, ages)
users = {"names": ["huoty", "esenich", "anan"], "ages": [18, 16, 8]}
"I am {names[0]}, age is {ages[0]}".format(**users)

# %% 指定转换
#  conversion ::= "r" | "s" | "a"
# 其中 "!r" 对应 repr()； "!s" 对应 str(); "!a" 对应 ascii()
"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')

# %% 对齐规则
print("{:>8}".format("181716"))
print("{:0>8}".format("181716"))
print("{:->8}".format("181716"))
print("{:-<8}".format("181716"))
print("{:-^8}".format("181716"))
print("{:-<25}>".format("Here "))

# %% 浮点精度
print("[ {:.2f} ]".format(321.33345))
print('{: f}; {: f}'.format(3.141592657, -3.141592657))
print('{:-f}; {:-f}'.format(3.141592657, -3.141592657))
print('{:+.4f}; {:+.4f}'.format(3.141592657, -3.141592657))
# %% 截取字符串
# 截取字符串类似于浮点精度控制，只是不需要加 f 在指定是浮点数
print('{:.2}'.format("hello"))
print('{:.3}'.format("huayong"))

# %% 指定进制
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(18))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(18))
# %% 千位分隔符
print('{:,}'.format(1234567890))

# %% 百分数显示
print("progress: {:.2%}".format(19.88/22))

# %% 作为函数使用
email_f = "Your email address was {email}".format
print(email_f(email="123abc@gmail.com"))
# %% 转义大括号
print("The {} set is often represented as {{0}} ".format("empty"))

# %%
from datetime import datetime
import re

def formats(s):
    print('starting ....', s)
    start = datetime.now()
    if '亿' in s:
        print(int(float(s))* 100000000)
    elif '万' in s:
        print(int(float(s)) * 10000)
    else:
        print(int(float(s)))
    mid = datetime.now()
    print('total time--->', mid - start)
    if re.findall('亿', s):
        print(int(float(s) * 100000000))
    elif re.findall('万', s):
        print(int(float(s) * 10000))
    else:
        print(int(s))
    end = datetime.now()




if __name__ == "__main__":
    for s in ['120.23亿', '304.234万', '2132343']:
        formats(s)
