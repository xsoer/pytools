"""
date: 2019-02-22 18:20:30
排序代码集合
"""


def bubble_sort(a: list):
    """
    冒泡排序
    算法思路：需要有两个游标，第一个从大范围从头遍历；第二个从第一个游标的位置+1处开始往后遍历；
    第一个游标的值和第二个游标的值进行比较，如果第一个比第二个大，就调整位置
    时间复杂度：O(n^2)，最好：O(n)，最坏：O(n^2)
    空间复杂度：O(1)
    """
    cnt = len(a)
    for i in range(cnt-2):
        for j in range(cnt-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    # for i in range(1, cnt):
    #     for j in range(i-1, cnt-1):
    #         if a[j] > a[j+1]:
    #             a[j], a[j+1] = a[j+1] , a[j]

    # for i in range(cnt):
    #     for j in range(cnt)[i:]:
    #         if a[i] > a[j]:
    #             a[i], a[j] = a[j], a[i]


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    bubble_sort(a)
    print(a)
