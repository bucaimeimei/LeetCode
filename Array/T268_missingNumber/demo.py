'''
  268. 缺失数字
  题目描述
  给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
  示例 1:
  输入: [3,0,1]
  输出: 2
  示例 2:
  输入: [9,6,4,2,3,5,7,0,1]
  输出: 8
  说明:
  你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''

import random

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = len(nums)        
        result = []
        max_ = nums[nums.index(max(nums))]
        large_nums = random.sample(range(0,max_+1),max_+1)
        llen = len(large_nums)
        if len_ != llen:
            for i in large_nums:
                if i not in nums:
                    result.append(i)
        if len_ == llen:
            result.append(max_+1)  
        for j in result:
            return j
            
            
            
        
