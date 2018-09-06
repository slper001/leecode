# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     3Sum_15
   Description :  三数之和
   Author :       机器灵砍菜刀
   Init Date：          2018/9/5
-------------------------------------------------
"""
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import collections
        r = []
        if len(nums) <3:
            return r
        d = collections.Counter(nums)
        p,n = [],[]
        if d.get(0,0)>2:   # 大于等于三个0的情况
            r.append([0,0,0])
        for k in d.keys():
            if k>=0:
                p.append(k)
            else:
                n.append(k)
        for i in n:
            for j in p:
                tar = -i-j     # 遍历0减正减负的值
                if tar in d.keys():
                    if i<tar<j:   # 如果不做此判断，结果会重复
                        r.append([i,tar,j])
                    elif (tar==i or tar==j) and d.get(tar)>1:
                        r.append([i,tar,j])
        return r