#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = len(nums)
        for i in range(cnt - 1):
            for j in range(i+1, cnt):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]
