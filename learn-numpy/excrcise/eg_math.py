#%%
import numpy as np
import matplotlib.pyplot as plt

#%% sigmoid函数图像
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[sigmoid(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% tanh函数
def tanh(x):
    s1 = np.exp(x) - np.exp(-x)
    s2 = np.exp(x) + np.exp(-x)
    s = s1 / s2
    return s
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[tanh(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% ReLU函数
def relu(x):
    s = np.where(x < 0, 0, x)
    return s

x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[relu(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% softmax函数
def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    print("x_sum = ", x_sum)
    s = x_exp / x_sum
    return s
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[softmax(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像


#%% L1损失函数
def L1(yhat, y):
    loss = np.sum(abs(y - yhat))
    return loss

#%% L2损失函数
def L2(yhat, y):
    loss = np.sum(np.multiply((y - yhat), (y - yhat)))
    return loss


#%% 三角函数 sin
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[np.sin(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% 三角函数 cos
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[np.cos(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% 三角函数 tan
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[np.tan(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%% 三角函数 tanh
x=np.linspace(-10,10,5000)  #这个表示在-10到10之间生成1000个x值
y=[np.tanh(i) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
plt.show()  #绘制图像

#%%
"""
矩阵函数	说明
np.sin(a)	对矩阵a中每个元素取正弦,sin(x)
np.cos(a)	对矩阵a中每个元素取余弦,cos(x)
np.tan(a)	对矩阵a中每个元素取正切,tan(x)
np.arcsin(a)	对矩阵a中每个元素取反正弦,arcsin(x)
np.arccos(a)	对矩阵a中每个元素取反余弦,arccos(x)
np.arctan(a)	对矩阵a中每个元素取反正切,arctan(x)
np.exp(a)	对矩阵a中每个元素取指数函数,ex
np.sqrt(a)	对矩阵a中每个元素开根号√x

ndarray.min() / np.min(ndarray)
ndarray.max() / np.max(ndarray)
ndarray.mean() / np.mean(ndarray)
ndarray.sum() / np.sum(ndarray)
np.sort() 排序
np.argsort() 排序的索引

"""