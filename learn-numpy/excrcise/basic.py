import math
import numpy as np
import matplotlib.pyplot as plt

# %%
np.__version__
np.__config__.show()

# %% 创建一维数组
a = np.arange(10)

# %% 创建布尔数组。数组大小为 3*3，全部为 True
a = np.full((3, 3), True, dtype=bool)
print(a)
# 答案二：
b = np.ones((3, 3), dtype=bool)
print(b)
# %% 按要求抽取数组中的元素.原数组为一维数组，内容为从 0 到 9，抽取出所有奇数。
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1])

# %% 按要求修改数组中的元素（原地修改）.原数组为一维数组，内容为从 0 到 9，将所有奇数原地修改为 -1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 答案
arr[arr % 2 == 1] = -1
print(arr)

# %% 按要求修改数组中的元素（返回新数组）.原数组为一维数组，内容为从 0 到 9，返回一个该数组的拷贝，其中奇数修改为 -1
arr = np.arange(10)

# 答案
out = np.where(arr % 2 == 1, -1, arr)
print(out)

# %% 修改数组的形状.将给定的一维数组 reshape 为二维数组，其中新数组的行数为2。
arr = np.arange(10)

# 答案
arr1 = arr.reshape(2, -1)  # -1 表示自动计算该维度的大小
print(arr1)
# print(arr.resize(2))

# %% 合并数组（列方向）.将给定数组在列方向上合并。
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# 答案 1:
np.concatenate([a, b], axis=0)
# 答案 2:
np.vstack([a, b])
# 答案 3:
np.r_[a, b]

# %% 合并数组（水平方向）.将给定数组在水平方向上合并。
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# 答案 1:
np.concatenate([a, b], axis=1)
# 答案 2:
np.hstack([a, b])
# 答案 3:
np.c_[a, b]

# %% 创建数组（进阶）.不用硬编码，使用内置方法，从给定数组 a 生成数组 b。
# 输入数组
a = np.array([1, 2, 3])
b = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

# 答案
np.r_[np.repeat(a, 3), np.tile(a, 3)]

# %% 返回公共元素.给定两个数组，要求返回这两个数组元素的交集。
# 输入数组
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# 答案：
np.intersect1d(a, b)
# > array([2, 4])

# %% 删除元素。给定两个数组 a、b，从数组 a 中删除 b 中出现的元素
# 输入数组
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

# 答案
np.setdiff1d(a, b)
# > array([1, 2, 3, 4])

# %% 找出相同元素。给定两个数组 a、b，返回两数组中相同元素的下标。
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# 答案：
np.where(a == b)
# > (array([1, 3, 5, 7]),)

# %% 按要求取出元素。从数组中取出大于等于 5 且小于等于 10 的元素。
# 输入数组
a = np.arange(15)

# 答案 1:
index = np.where((a >= 5) & (a <= 10))
a[index]

# 答案 2:
index = np.where(np.logical_and(a >= 5, a <= 10))
a[index]

# 答案 3:
a[(a >= 5) & (a <= 10)]
# > (array([6, 9, 10]),)

# %% 实现 max 的 numpy 版。
# 给定长度相同的数组 a、b，返回一个新数组，数组上的每一个元素为 max(a_i, b_i)。
# 输入数组


def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


pair_max = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a, b)

# > 期望输出：array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])

# 答案:


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max(a, b)

# %% 交换二维数组的列。交换数组的第一第二列。
# 输入数组
arr = np.arange(9).reshape(3, 3)

# 答案:
arr[:, [1, 0, 2]]
# > array([[1, 0, 2],
# >        [4, 3, 5],
# >        [7, 6, 8]])

# %% 交换二维数组的行。交换二维数组的第一第二行。
# 输入数组
arr = np.arange(9).reshape(3, 3)

# 答案
arr[[1, 0, 2], :]
# > array([[3, 4, 5],
# >        [0, 1, 2],
# >        [6, 7, 8]])

# %% 将一个数组按行反序。数组 arr 为二维数组，将其行反序
# 输入数组
arr = np.arange(9).reshape(3, 3)

# 答案:
arr[::-1]

# %% 将一个数组按列反序。数组 arr 为二维数组，将其列反序。
# # 输入数组
arr = np.arange(9).reshape(3, 3)

# 答案:
arr[:, ::-1]


# %% 创建随机数组。创建一个 5*3 的数组，数组元素为 5 到 10 的随机浮点数
# 答案 1:
rand_arr = np.random.randint(
    low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
# print(rand_arr)
# 答案 2:
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)
# >[[6.36562219 9.59578896 7.61792658]
# > [6.92537094 7.32734944 8.75144393]
# > [6.83628625 7.17482099 8.79405102]
# > [7.87810626 6.61146893 6.6438487 ]
# > [5.81711252 6.80231869 7.87766307]]

# %% 按要求打印数组（一）.数组元素输出时保留 3 位小数。
# 输入数组
rand_arr = np.random.random([5, 3])

# 答案：
# 设置保留 3 位小数
np.set_printoptions(precision=3)
rand_arr[:4]

# %% 按要求打印数组（二）.数组为小数，使用小数点的形式来打印，而不是科学记数法（如1e-4）。
# 输入数组
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
rand_arr
# > array([[  5.434049e-04,   2.783694e-04,   4.245176e-04],
# >        [  8.447761e-04,   4.718856e-06,   1.215691e-04],
# >        [  6.707491e-04,   8.258528e-04,   1.367066e-04]])

# 答案:
np.set_printoptions(suppress=True, precision=6)  # precision 是可选项
rand_arr

# %% 按要求打印数组（三）。打印时省略中间元素，限制显示数组元素的个数为 6。
a = np.arange(15)
# > 原输出 ：[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]
# > 目标输出：[ 0  1  2 ..., 12 13 14] array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

# 答案:
np.set_printoptions(threshold=6)
print(a)
# %% 加载特殊矩阵.著名的 iris 数据集是包含兰花属性和种类的数据集，其中每行属性有数字和文字，用 numpy 来加载他们。
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# 输出前三行
iris[:3]

# %% 重定义数组的元素范围.
# np.zeros((784, 1))
# np.random.randn(30, 784)
np.random.randn(30, 1)
# np.zeros((30, 784))


# %% dot实例
# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# 2-D array: 3 x 2
two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
print('two_multi_res: %s' % (two_multi_res))

"""
矩阵的点积
    就是矩阵各个对应元素相乘, 这个时候要求两个矩阵必须同样大小

矩阵的乘法
    就是矩阵a的第一行乘以矩阵b的第一列，各个元素对应相乘然后求和作为第一元素的值。
    矩阵只有当左边矩阵的列数等于右边矩阵的行数时,它们才可以相乘,乘积矩阵的行数等于左边矩阵的行数,乘积矩阵的列数等于右边矩阵的列数
卷积
把模板（n*n）放在矩阵上（中心对准要处理的元素），用模板的每个元素去乘矩阵中的的元素，累加和等于这个元素。步骤很简单：
    1.求卷积矩阵的元素x,y时，对准h矩阵的x,y元素。
    2.然后 f 矩阵从1,1朝右朝下移动，h从x,y朝左朝上移动。
    3.对应元素相乘、相加即可。
"""

# %% 点乘、dot、multiply
A = np.arange(1, 5).reshape(2, 2)
B = np.arange(0, 4).reshape(2, 2)
# print(A)
# print(B)
# 数组对应元素位置相乘
print(np.multiply(A, B))
# mat把数组转换成矩阵。multiply永远是对应位置相乘
print(np.multiply(np.mat(A), np.mat(B)))
# 输出标量。
np.sum(np.multiply(np.mat(A), np.mat(B)))
# 对数组执行矩阵相乘运算。dot永远是执行矩阵乘法运算。
np.dot(A, B)
# 执行矩阵乘法运算
np.dot(np.mat(A), np.mat(B))
# 对应位置点乘。数组乘数组就是对应位置的点乘
A*B
# 执行矩阵运算。矩阵乘矩阵就是对应矩阵的乘法运算
(np.mat(A))*(np.mat(B))

C = np.arange(1, 4)
D = np.arange(0, 3)
print(C)
print(D)
# 对应位置相乘，再求和
np.dot(C, D)

# %% nan、inf to num

a = np.array([[np.nan, np.inf], [-np.nan, -np.inf]])
np.nan_to_num(a)

"""
一组判别函数
    isinf
    isneginf
    isposinf
    isnan
    isfinite
"""
# 例如 isnan来判断是否是nan
np.isnan(np.array([[1, np.nan, np.inf], [np.nan, -np.inf, -0.25]]))
# %% where寻找下标
a = np.linspace(-5, 5, 10000)
b = a * a
x0 = 4
y0 = 4
num = np.linspace(0, len(a) - 1, len(a))
dis = np.linspace(0, 0, len(a))
for k in num:
    k = int(k)
    dis[k] = dis[k] + math.sqrt((a[k] - x0) ** 2 + (b[k] - y0) ** 2)
disMin = min(dis)
disMinIndex = np.where(dis == disMin)
disMin0 = math.sqrt((a[disMinIndex] - x0) ** 2 + (b[disMinIndex] - y0) ** 2)
print('The mininum distance:', disMin)
print('The mininum distance:', disMin0)
print(type(dis))
a0 = a[disMinIndex]
b0 = b[disMinIndex]
fig = plt.figure(figsize=(6, 6), dpi=200)
ax1 = plt.subplot(1, 1, 1)
line11 = ax1.scatter(a, b, s=1)
line12 = ax1.scatter(x0, y0, s=100, marker='*', color='darkorange')
line13 = ax1.scatter(a0, b0, s=100, marker='*', color='darkorange')
line14 = ax1.plot([x0, a0], [y0, b0], color='darkorange')
line15 = ax1.text(4.2, 4, 'Q(x0,y0)')
line16 = ax1.text(0.6, 5, 'M(a0,b0)')
line18 = plt.xlim(-5, 5)
line17 = plt.ylim(0, 25)
# plt.savefig('index.png')
plt.show()


# %% 最值
a = np.arange(9).reshape((3, 3))
print(a)
# 全局最大
print(np.max(a))
# 每列最大
print(np.max(a, axis=0))
# 每行最大值
print(np.max(a, axis=1))
# 打印最大值的位置
print(np.where(a==np.max(a)))
print(np.where(a==np.max(a,axis=0)))
# %%
