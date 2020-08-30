"""
date: 2019-02-25 10:30
排序代码集合
"""


class node:
    def __init__(self, k):
        self.key = k
        self.next = None


def bucket_sort(lista):
    h = []
    for i in range(0, 10):
        h.append(node(0))
    for i in range(0, len(lista)):
        tmp = node(lista[i])
        map = lista[i]//10
        p = h[map]
        if p.key is 0:
            h[map].next = tmp
            h[map].key = h[map].key+1
        else:
            while(p.next != None and p.next.key <= tmp.key):
                p = p.next
            tmp.next = p.next
            p.next = tmp
            h[map].key = h[map].key+1
    k = 0
    for i in range(0, 10):
        q = h[i].next
        while(q != None):
            lista[k] = q.key
            k = k+1
            q = q.next


if __name__ == '__main__':
    a = [2, 1, 4, 6, 3, 45, 76, 47, 34, 5, 23]
    bucket_sort(a)
    print(a)
