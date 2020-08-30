import numpy as np

#%% No Copy at All

# Simple assignments make no copy of array objects or of their data.
a = np.arange(12)
b = a
print('b is a\n', b is a)

b.shape = 3, 4
print('a.shape\n', a.shape)

# Python passes mutable objects as references, so function calls make no copy.
def f(x):
    print(id(x))
print('id(a)\n',id(a))
print('f(a)\n',f(a))

#%% View or Shallow Copy

# Different array objects can share the same data. The view method creates a new array object that looks at the same data.
c = a.view()
print('c is a\n', c is a)
print('c.base is a\n',c.base is a)
print('c.flags.owndata\n',c.flags.owndata)

c.shape = 2,6
print('a.shape\n',a.shape)
c[0,4] = 1234 # a's data changes
print('a\n',a)

# Slicing an array returns a view of it:
s = a[ : , 1:3] # spaces added for clarity; could also be written "s = a[:,1:3]
s[:] = 10 # # s[:] is a view of s. Note the difference between s=10 and a[:]=10
print('a\n',a)


#%% Deep Copy
d = a.copy() # a new array object with new data is created
print('d is a\n', d is a)
print('d.base is a\n',d.base is a)
d[0,0] = 9999
print('a\n',a)

# Sometimes copy should be called after slicing if the original array is not required anymore. For example, suppose a is a huge intermediate result and the ﬁnal result b only contains a small fraction of a, a deep copy should be made when constructing b with slicing
a = np.arange(int(1e8))
b = a[:100].copy()
del a # the memory of ``a`` can be released

# If b = a[:100] is used instead, a is referenced by b and will persist in memory even if del a is executed.

#%% Functions and Methods Overview

"""
Here is a list of some useful NumPy functions and methods names ordered in categories. See routines for the full list.

Array Creation
    arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like

Conversions
    ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat

Manipulations
    array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack

Questions
    all, any, nonzero, where

Ordering
    argmax, argmin, argsort, max, min, ptp, searchsorted, sort

Operations
    choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask,real, sum

Basic Statistics
    cov, mean, std, var Basic Linear Algebra cross, dot, outer, linalg.svd, vdot
"""