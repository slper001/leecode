# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     3SumClosest_16
   Description : 最接近的三数之和
   Author :       机器灵砍菜刀
   Init Date：          2018/9/6
-------------------------------------------------
"""
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        temp_diff = float('inf')
        res = 0
        for i in range(n):
            left_point = i+1
            right_point = n-1
            while left_point < right_point:
                s = nums[left_point] + nums[right_point]+nums[i]
                diff = s-target
                if diff == 0:
                    return s
                if abs(diff)<temp_diff:
                    res = s
                    temp_diff = abs(diff)
                if diff<0:
                    left_point +=1
                else:
                    right_point -=1
        return res



