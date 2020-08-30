"""
date: 2019-02-24 15:20:30
排序代码集合
"""


def selection_sort(a: list):
    """
    选择排序

    """
    cnt = len(a)
    if not cnt:
        return a
    for i in range(cnt):
        minIndex = i
        for j in range(cnt)[i:]:
            if a[j] < a[minIndex]:
                a[minIndex], a[j] = a[j], a[minIndex]
    return a


if __name__ == "__main__":
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    selection_sort(a)
    print(a)
