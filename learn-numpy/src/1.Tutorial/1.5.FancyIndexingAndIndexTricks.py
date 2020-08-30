import numpy as np
"""
NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, as we saw before, arrays can be indexed by arrays of integers and arrays of booleans.
"""
# %% Indexing with Arrays of Indices
a = np.arange(12) ** 2  # the first 12 square numbers
i = np.array([1, 1, 3, 8, 5])  # an array of indices
print('a[i]\n', a[i])  # the elements of a at the positions i

j = np.array([[3, 4], [9, 7]])
print('a[j]\n', a[j])

# When the indexed array a is multidimensional, a single array of indices refers to the ﬁrst dimension of a. The following example shows this behavior by converting an image of labels into a color image using a palette.
palette = np.array([[0, 0, 0], [255, 0, 0], [0, 255, 0],
                    [0, 0, 255], [255, 255, 255]])
image = np.array([[0, 1, 2, 0], [0, 3, 4, 0]])
print('palette[image]\n', palette[image])

# We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.
a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1],                        # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],                        # indices for the second dim
              [3, 3]])
print('a[i,j]\n', a[i, j])  # i and j must have equal shape
print('a[i,2]\n', a[i, 2])
print('a[:,j]\n', a[:, j])

# Naturally, we can put i and j in a sequence (say a list) and then do the indexing with the list.
l = [i,j]
print('a[l]\n',a[l])

# Another common use of indexing with arrays is the search of the maximum value of time-dependent series:
time = np.linspace(20, 145, 5)                 # time scale
data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series
print('time\n', time)
print('data\n', data)
ind = data.argmax(axis=0)                  # index of the maxima for each series
print('ind\n', ind)

time_max = time[ind]                       # times corresponding to the maxima
data_max = data[ind, range(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
print('time_max\n', time_max)
print('data_max\n', data_max)
np.all(data_max == data.max(axis=0))


# You can also use indexing with arrays as a target to assign to:
a = np.arange(5)
print('a', a)
a[[1,3,4]] = 0
print('a', a)

# However, when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value:
a = np.arange(5)
a[[0,0,2]]=[1,2,3]
print('a\n', a)

# This is reasonable enough, but watch out if you want to use Python’s += construct, as it may not do what you expect:
a = np.arange(5)
a[[0,0,2]]+=1
print('a\n', a)

# %% Indexing with Boolean Arrays

# When we index arrays with arrays of (integer) indices we are providing the list of indices to pick. With boolean indices the approach is different; we explicitly choose which items in the array we want and which ones we don’t.

# The most natural way one can think of for boolean indexing is to use boolean arrays that have the same shape as the original array:
a = np.arange(12).reshape(3,4)
b = a > 4
print('b\n',b)                                          # b is a boolean with a's shape
print('a[b]\n',a[b])                                       # 1d array with the selected elements

# This property can be very useful in assignments:
a[b] = 0                                   # All elements of 'a' higher than 4 become 0
print('a\n', a)

# You can look at the following example to see how to use boolean indexing to generate an image of the Mandelbrot set:
import matplotlib.pyplot as plt
def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime
plt.imshow(mandelbrot(400,400))
plt.show()

# The second way of indexing with booleans is more similar to integer indexing; for each dimension of the array we give a 1D boolean array selecting the slices we want:
a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])             # first dim selection
b2 = np.array([True,False,True,False])       # second dim selection

print('a[b1,:]\n',a[b1,:])                                   # selecting rows
print('a[b1,:]\n',a[b1,:])                                     # same thing
print('a[:,b2]\n',a[:,b2])                                   # selecting columns
print('a[b1,b2]\n',a[b1,b2])                                  # a weird thing to do

#%% The ix_() function

# The ix_ function can be used to combine different vectors so as to obtain the result for each n-uplet. For example, if you want to compute all the a+b*c for all the triplets taken from each of the vectors a, b and c:
a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])
ax,bx,cx = np.ix_(a,b,c)
print('ax\n',ax)
print('bx\n',bx)
print('cx\n',cx)
print('ax.shape\n',ax.shape)
print('bx.shape\n',bx.shape)
print('cx.shape\n',cx.shape)
result = ax+bx*cx
print('result\n',result)
print('result[3,2,4]\n',result[3,2,4])
print('a[3]+b[2]*c[4]\n',a[3]+b[2]*c[4])

# You could also implement the reduce as follows:
def ufunc_reduce(ufct, *vectors):
   vs = np.ix_(*vectors)
   r = ufct.identity
   for v in vs:
       r = ufct(r,v)
   return r

print('ufunc_reduce(np.add,a,b,c)\n',ufunc_reduce(np.add,a,b,c))

#%%
