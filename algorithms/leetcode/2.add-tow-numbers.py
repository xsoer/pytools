#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" 测试用例要写好，多考虑些情况
    比如l1和l2相等长度，
    l1和l2不等长度

    考察点：链表如何遍历，

    列表最后一个不能为0，也就是数字首字母不能为0
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        l3 = head
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            add = v1 + v2 + carry

            if add < 10:
                l3.val = add
                carry = 0
            else:
                l3.val = add % 10
                carry = 1
            # print(l3.val)
            # 判断是否有进位
            if carry:
                l3.next = ListNode(1)
                l3 = l3.next

            # 判断是否还需要添加,需要先判断l1和l2是否存在，在判断其是否有next值
            elif (l1 and l1.next) or (l2 and l2.next):
                l3.next = ListNode(0)
                l3 = l3.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 进行打印
        # t_head = head
        # while t_head:
        #     print(t_head.val)
        #     t_head = t_head.next
        # 要返回链的首部，而不是最后一个元素
        return head
# @lc code=end
