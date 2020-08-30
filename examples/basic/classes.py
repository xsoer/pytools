# 数据属性会覆盖掉具有相同名称的方法属性；为了避免会在大型程序中导致难以发现的错误的意外名称冲突，明智的做法是使用某种约定来最小化冲突的发生几率。 可能的约定包括方法名称使用大写字母，属性名称加上独特的短字符串前缀（或许只加一个下划线），或者是用动词来命名方法，而用名词来命名数据属性
#%%
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

"""
Python有两个内置函数可被用于继承机制：
    使用 isinstance() 来检查一个实例的类型: isinstance(obj, int) 仅会在 obj.__class__ 为 int 或某个派生自 int 的类时为 True。
    使用 issubclass() 来检查类的继承关系: issubclass(bool, int) 为 True，因为 bool 是 int 的子类。 但是，issubclass(float, int) 为 False，因为 float 不是 int 的子类。


finally 子句 总会在离开 try 语句前被执行，无论是否发生了异常。 当在 try 子句中发生了异常且尚未被 except 子句处理（或者它发生在 except 或 else 子句中）时，它将在 finally 子句执行后被重新抛出。 当 try 语句的任何其他子句通过 break, continue 或 return 语句离开时，finally 也会在“离开之前”被执行，
"""


#%%
class Base(object):
    def __init__(self):
        self.db = 'bac'

    def show_db(self):
        print('base db--->',self.db)

class A(Base):
    def __init__(self):
        Base.__init__(self)
        # super(A).__init__()
        self.a = 'aaa'

    def show_a(self):
        print('A--->',self.a)

    def show_base(self):
        print('A base--->',self.db)

a = A()
a.show_a()
a.show_base()
a.show_db()

# %%
