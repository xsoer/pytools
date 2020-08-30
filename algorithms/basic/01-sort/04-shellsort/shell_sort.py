
"""
date: 2019-02-22 18:20:30
排序代码集合
"""


def shell_sort(a: list):
    """
    希尔排序
    算法思路：
    时间复杂度：O(n^2)，最好：O(n)，最坏：O(n^2)
    空间复杂度：O(1)
    """
    cnt = len(a)
    if not cnt:
        return a
    gap = cnt // 2
    while gap > 0:
        for i in range(gap, cnt, 1):
            tmp = a[i]
            pre_index = i - gap
            while pre_index >= 0 and a[pre_index] > tmp:
                a[pre_index+gap] = a[pre_index]
                pre_index -= gap
            a[pre_index+gap] = tmp
        gap //= 2
    return a


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    shell_sort(a)
    print(a)
