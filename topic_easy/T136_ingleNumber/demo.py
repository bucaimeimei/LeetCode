'''
    136. 只出现一次的数字
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    示例 1:
        输入: [2,2,1]
        输出: 1
    示例 2:
        输入: [4,1,2,1,2]
        输出: 4
'''


class Solution(object):
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #利用列表操作方法
        apaxes_list = []
        for i in nums:
            if i not in apaxes_list:
                apaxes_list.append(i)
            else:
                apaxes_list.remove(i)
        return apaxes_list.pop()

if __name__ == "__main__":
    solution = Solution()
    print("--------利用列表方法--------")
    arr1 = [2,2,1]
    res = solution.singleNumber_1(arr1)
    print(res)
    arr2 = [4,1,2,1,2]
    res = solution.singleNumber_1(arr2)
    print(res)
