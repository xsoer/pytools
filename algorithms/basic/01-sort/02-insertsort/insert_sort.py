

def insert_sort(a: list):
    """
    插入排序
    算法思路：
    时间复杂度：
    空间复杂度：
    """
    cnt = len(a)
    if not cnt:
        return a

    for i in range(cnt - 1):
        value = a[i+1]
        pre_index = i
        while (pre_index >= 0 and value < a[pre_index]):
            a[pre_index + 1] = a[pre_index]
            pre_index -= 1
        a[pre_index+1] = value
    return a


if __name__ == "__main__":
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    insert_sort(a)
    print(a)
