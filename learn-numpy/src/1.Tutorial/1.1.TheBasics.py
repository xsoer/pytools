# %%

from numpy import pi
import numpy as np

"""
NumPy’s array class is called ndarray.
"""

"""
ndarray.ndim
    the number of axes (dimensions) of the array.

ndarray.shape
    the dimensions of the array. This is a tuple of integers indicating the size of the array in each di-mension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.

ndarray.size
    the total number of elements of the array. This is equal to the product of the elements of shape. ndarray.dtype an object describing the type of the elements in the array. One can create or specify dtype’s us-ing standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.ﬂoat64 are some examples.

ndarray.itemsize
    the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

ndarray.data
    the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
"""

# %% 2.2.1 An example
a = np.arange(15).reshape(3, 5)
print('a', a)
print('a.size', a.size)
print('a.ndim', a.ndim)
print('a.dtype', a.dtype)
print('a.dtype.name', a.dtype.name)
print('a.itemsize', a.itemsize)
print('type(a)', type(a))

# %% 2.2.2 Array Creation
# a = np.array(2,3,4) wrong
a = np.array([2, 3, 4])
print('a.dtype', a.dtype)

b = np.array([1.2, 3.5, 5.1])
print('b.dtype', b.dtype)

c = np.array([(1.5, 2, 3), (4, 5, 6)])

d = np.array([[1, 2], [3, 4]], dtype=complex)
print('d', d)

e = np.zeros((3, 4))
print('e', e)

f = np.ones((2, 3, 4), dtype=np.int16)
print('f', f)

g = np.empty((2, 3))
print('g', g)

h = np.arange(10, 30, 5)
print('h', h)

i = np.arange(0, 2, 0.3)  # accept float
print('i', i)

j = np.linspace(0, 2, 9)
print('j', j)

k = np.linspace(0, 2 * pi, 100)
print('k', k)

l = np.sin(k)
print('l', l)

# array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, numpy. random.rand, numpy.random.randn, fromfunction, fromfile

# %% 2.2.3 Printing Arrays
"""
1.the last axis is printed from left to right
2.the second-to-last is printed from top to bottom
3.the rest are also printed from top to bottom, with each slice separated from the next by an empty line
"""
print(np.arange(10000).reshape(100, 100))
np.set_printoptions(threshold=np.nan)

# %% 2.2.4 Basic Operations

# Arithmetic operators on arrays apply elementwise. A new array is created and ﬁlled with the result.
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a-b
print('c', c)
print('b**2\n', b ** 2)
print('10 * np.sin(a)\n', 10 * np.sin(a))
print('a<35\n', a < 35)

# Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method:
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print('A*B\n', A * B)
print('A@B\n', A @ B)
print('A.dot(B)\n', A.dot(B))

# Some operations, such as += and * =, act in place to modify an existing array rather than create a new one.
a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
print('a\n', a)
b += a
print('b\n', b)
# a += b #b is not automatically converted to integer type.raise ValueError

# When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print('b.dtype.name\n', b.dtype.name)

c = a+b
print('c\n', c)
print('c.dtype.name\n', c.dtype.name)

d = np.exp(c * 1j)
print('d\n', d)
print('d.dtype.name\n', d.dtype.name)

# Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class.

a = np.random.random((2, 3))
print('a\n', a)
print('a.sum\n', a.sum())
print('a.min()', a.min())
print('a.max()', a.max())

# By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the axis parameter you can apply an operation along the speciﬁed axis of an array

b = np.arange(12).reshape(3, 4)
print('b\n', b)
print('b.sum(axis=0)\n', b.sum(axis=0))
print('b.min(axis=1)\n', b.min(axis=1))
print('b.cumsum(axis=1)', b.cumsum(axis=1))

# %% 2.2.5 Universal Functions
# NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions”(ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.
B = np.arange(3)
print('B\n', B)
print('np.exp(B)\n', np.exp(B))
print('np.sqrt(B)\n', np.sqrt(B))

C = np.array([2., -1., 4.])
print('np.add(B, C)\n', np.add(B, C))

"""
# See also:

all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where
"""


# %% 2.2.6 Indexing, Slicing and Iterating

# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences\
a = np.arange(10) ** 3
print('a\n', a)
print('a[2]\n', a[2])
print('a[2:5]\n', a[2:5])

a[:6:2] = -1000  # equivalent to a[0:6:2] = -1000; from start to position 6, ˓→exclusive, set every 2nd element to -1000
print('a\n', a)
print('a[ : :-1]\n', a[::-1])

for i in a:
    print(i ** (1/3.))

# Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:


def ff(x, y):
    return 10 * x+y


b = np.fromfunction(ff, (5, 4), dtype=int)
print('b\n', b)
print('b[2,3]\n', b[2, 3])
print('b[0:5, 1]\n', b[0:5, 1])  # each row in the second column of b
print('b[ : ,1]\n', b[:, 1])  # equivalent to the previous example
# each column in the second and third row of b
print('b[1:3, : ]\n', b[1:3, :])

"""
The dots (...) represent as many colons as needed to produce a complete indexing tuple. For example, if x is an array with 5 axes, then
    • x[1,2,...] is equivalent to x[1,2,:,:,:],
    • x[...,3] to x[:,:,:,:,3] and
    • x[4,...,5,:] to x[4,:,:,5,:].
"""
c = np.array([[[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]])
print('c.shape\n', c.shape)
print('c[1,...]\n', c[1, ...])
print('c[...,2]\n', c[..., 2])

# However, if one wants to perform an operation on each element in the array, one can use the flat attribute which is an iterator over all the elements of the array:
for element in b.flat:
    print(element)

"""
See also:
    Indexing, arrays.indexing (reference), newaxis, ndenumerate, indices
"""

# %%
