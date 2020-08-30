#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)[::-1]
        if a[-1] == '-':
            x =  -1*int(a[:-1])
        else:
            x =  int(a)
        if x >= (2**31 -1) or x <= (-2**31):
            return 0
        else:
            return x

