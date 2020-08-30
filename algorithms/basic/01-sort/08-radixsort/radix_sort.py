"""
date: 2019-02-25 10:30
排序代码集合
"""

import math


def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j//(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    radix_sort(a)
    print(a)
