'''
  104. 二叉树的最大深度
  题目描述：
  给定一个二叉树，找出其最大深度。
  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
  说明: 叶子节点是指没有子节点的节点。
  示例：
  给定二叉树 [3,9,20,null,null,15,7]，
      3  
     / \   
    9  20  
      /  \   
     15   7   
  返回它的最大深度 3 。
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        '''
    
        方法一：非递归实现的BFS
        '''
        if root is None:
            return 0
        
        # initialize the queue and lenth
        queue = collections.deque()
        queue.append(root)
        lenth = 0
        
        # loop over the queue 
        while queue:
            lenth += 1
            for i in range(len(queue)):
                # print("lenth:{}, i:{}".format(lenth, i))
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        return lenth

        
        
      
