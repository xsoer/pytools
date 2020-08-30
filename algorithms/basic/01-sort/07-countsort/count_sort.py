"""
date: 2019-02-25 10:19
排序代码集合
"""


def count_sort(array):
    leng = len(array)
    c = []
    res = []
    for i in range(0, 100):
        c.append(0)
    for i in range(0, leng):
        c[array[i]] = c[array[i]]+1
        res.append(0)
    for i in range(0, 100):
        c[i] = c[i-1]+c[i]
    for i in range(leng-1, -1, -1):
        res[c[array[i]]-1] = array[i]
        c[array[i]] = c[array[i]]-1
    return res;


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    print(count_sort(a))
