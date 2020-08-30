
"""
date: 2019-02-22 18:20:30
排序代码集合
"""


def merge_sort(a: list):
    """
    归并排序
    算法思路：
    时间复杂度：O(n^2)，最好：O(n)，最坏：O(n^2)
    空间复杂度：O(1)
    """
    cnt = len(a)
    if cnt < 2:
        return a
    mid = cnt // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def merge(left: list, right: list):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    print(merge_sort(a))
