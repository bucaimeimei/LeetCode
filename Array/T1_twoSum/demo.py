'''
  题目说明:
  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
  示例:
  给定 nums = [2, 7, 11, 15], target = 9
  因为 nums[0] + nums[1] = 2 + 7 = 9
  所以返回 [0, 1]
'''

class Solution(object):
    #方法1
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_num = len(nums)
        j=-1
        for i in range(len_num):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):
                    #如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                else:
                    j = nums.index(target - nums[i],i+1) 
                    #index(x,i+1)是从num1后的序列后找num2        
                    break
        if j>0:
            return [i,j]
        else:
            return []
            
    #方法2        
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]+nums[j] == target:
                    r.append(i)
        return r
      
if __name__ == "__main__":
    solution = Solution()
    target = 9
    arr1 = [2, 7, 11, 15]
    res = solution.twoSum1(arr1，target)
    print(res)
