
import numpy as np

# %% 2.3.1 Changing the shape of an array

# An array has a shape given by the number of elements along each axis:
a = np.floor(10 * np.random.random((3, 4)))
print('a\n', a)
print('a.shape\n', a.shape)
print('a.ravel()\n', a.ravel())  # returns the array, flattened
print('a.reshape(6,2)\n', a.reshape(6, 2))
print('a.T\n', a.T)
print('a.T.shape\n', a.T.shape)
print('a.shape\n', a.shape)

# The reshape function returns its argument with a modiﬁed shape, whereas the ndarray.resize method modiﬁes the array itself
a.resize((2, 6))
print('a\n', a)

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
a.reshape(3, -1)
print('a\n', a)
"""
See also:
    ndarray.shape, reshape, resize, ravel
"""

# %% Stacking together different arrays

# Several arrays can be stacked together along different axes
a = np.floor(10 * np.random.random((2, 2)))
print('a\n', a)
b = np.floor(10 * np.random.random((2, 2)))
print('b\n', b)
print('np.vstack((a,b))\n', np.vstack((a, b)))
print('np.hstack((a,b))\n', np.hstack((a, b)))

from numpy import newaxis
# The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D arrays:
np.column_stack((a, b))
a = np.array([4., 2.])
b = np.array([3., 8.])
print('np.column_stack((a,b))\n', np.column_stack((a, b)))  # returns a 2D array
print('np.hstack((a,b))\n', np.hstack((a, b)))
print('a[:,newaxis]\n', a[:, newaxis])
print('np.column_stack((a[:,newaxis],b[:,newaxis]))\n',
      np.column_stack((a[:, newaxis], b[:, newaxis])))
print('np.hstack((a[:,newaxis],b[:,newaxis]))\n',
      np.hstack((a[:, newaxis], b[:, newaxis])))

# On the other hand, the function row_stack is equivalent to vstack for any input arrays. In general, for arrays of with more than two dimensions, hstack stacks along their second axes, vstack stacks along their ﬁrst axes, and concatenate allows for an optional arguments giving the number of the axis along which the concatenation should happen.
# In complex cases, r_ and c_ are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals (“:”)
print('np.r_[1:4,0,4]\n',np.r_[1:4,0,4])
# When used with arrays as arguments, r_ and c_ are similar to vstack and hstack in their default behavior, but allow for an optional argument giving the number of the axis along which to concatenate.
"""
See also:
    hstack, vstack, column_stack, concatenate, c_, r_
"""

# %% Splitting one array into several smaller ones

# Using hsplit, you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur:
a = np.floor(10 * np.random.random((2,12)))
print('a\n',a)
print('np.hsplit(a,3)\n',np.hsplit(a,3))
print('np.hsplit(a,(3,4))\n',np.hsplit(a,(3,4)))

# vsplit splits along the vertical axis, and array_split allows one to specify along which axis to split