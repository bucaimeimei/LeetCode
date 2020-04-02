'''
  #234. 回文链表
  题目描述
  请判断一个链表是否为回文链表。
  示例 1:
  输入: 1->2
  输出: false
  示例 2:
  输入: 1->2->2->1
  输出: true
  进阶：
  你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
