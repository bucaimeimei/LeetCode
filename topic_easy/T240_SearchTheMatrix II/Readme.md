#240. 搜索二维矩阵 II
=====================

难度: 中等
----------


题目描述
---------

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

1.每行的元素从左到右升序排列。

2.每列的元素从上到下升序排列。

说明
----

示例:

现有矩阵 matrix 如下：


[

  [1,   4,  7, 11, 15],
  
  [2,   5,  8, 12, 19],
  
  [3,   6,  9, 16, 22],
  
  [10, 13, 14, 17, 24],
  
  [18, 21, 23, 26, 30]
  
]


给定 target = 5，返回 true。

给定 target = 20，返回 false。

解题思路
--------

方法1：字典方法
--------------

思路：
-----

1.创建一个字典记录true的出现次数

2.判断true的出现次数大于1时，返回true。等于0时返回false


复杂度计算：
----------

1.时间复杂度：

2.空间复杂度：

执行用时：
--------

244 ms  在所有 Python 提交中击败了13.72%的用户


内存消耗：
--------

16.6 MB, 在所有 Python 提交中击败了5.31%的用户

优化方向：
---------

1.

2.