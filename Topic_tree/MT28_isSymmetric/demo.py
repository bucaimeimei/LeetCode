'''
面试题28. 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
 
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
 
限制：
0 <= 节点个数 <= 1000
'''

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isSyt(left_,right_):
            if not left_ and not right_:#节点都为空,也是对称的
                return True
            elif left_ and right_:#都不为空
                if left_.val != right_.val:#不为空且不相等则不是对称的
                    return False
                else:
                    return isSyt(left_.right, right_.left) and isSyt                                (left_.left, right_.right)#遍历左右子树
            else:#一个节点为空一个节点不为空
                return False
        return isSyt(root.left, root.right)

