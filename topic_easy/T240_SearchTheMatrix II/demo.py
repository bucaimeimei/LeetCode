'''
  240. 搜索二维矩阵 II
  编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
  1.每行的元素从左到右升序排列。
  2.每列的元素从上到下升序排列。
  说明
  示例:
  现有矩阵 matrix 如下：
  [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
  ]
  给定 target = 5，返回 true。
  给定 target = 20，返回 false。
'''

class Solution(object):
    #方法1
    def searchMatrix_1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        tf_dict={}
        tf_dict['true']= 0
        tf_dict['false']= 0
        for i_list in matrix:
            for i in i_list:
                if i == target:
                    tf_dict['true'] += 1
        if tf_dict['true']>1:
            return True
        if tf_dict['true'] ==1:
            return True
        if tf_dict['true'] ==0:  
            return False
if __name__ == "__main__":
  solution = Solution()
  print("--------利用字典方法--------")
  matrix = [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
  ]
  target1=5
  res = solution.searchMatrix_1(matrix,target1)
  print(res)
  target2=20
  res = solution.searchMatrix_1(matrix,target2)
  print(res)
