#160. 相交链表
==============

编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：

在节点 c1 开始相交。
 
示例 1：

输入：

intersectVal = 8, 

listA = [4,1,8,4,5], 

listB = [5,0,1,8,4,5], 

skipA = 2, 

skipB = 3

输出：

Reference of the node with value = 8

输入解释：

相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。

从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。

在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 
示例 2：

输入：

intersectVal = 2, 

listA = [0,9,1,2,4],

listB = [3,2,4], 

skipA = 3,

skipB = 1

输出：

Reference of the node with value = 2

输入解释：

相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。

从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。

在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 
示例 3：

输入：

intersectVal = 0, 

listA = [2,6,4], 

listB = [1,5], 

skipA = 3, 

skipB = 2

输出：null

输入解释：

从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。

由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。

解释：这两个链表不相交，因此返回 null。
 
注意：
------

如果两个链表没有交点，返回 null.

在返回结果后，两个链表仍须保持原有的结构。

可假定整个链表结构中没有循环。

程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

解题思路：
---------

方法1：双指针法
---------

初始化 pA = headA, pB = headB，开始遍历。

pA会先到达链表尾，当pA到达末尾时，重置pA为headB；同样的，当pB到达末尾时，重置pB为headA。当pA与pB相遇时，必然就是两个链表的交点。

为什么要这样处理？因为这样的一个遍历过程，对pA而言，走过的路程即为a+c+b，对pB而言，即为b+c+a，显然a+c+b = b+c+a，这就是该算法的核心原理。

即使两个链表没有相交点，事实上，仍然可以统一处理，因为这种情况意味着相交点就是null，也就是上图中的公共部分c没有了，从而递推式变成了pA: a+b，pB: b+a，这同样是成立的。

复杂度分析
---------

时间复杂度：O（m+n）

空间复杂度：O(1)

方法2: 哈希表法
---------------

遍历链表 A 并将每个结点的地址/引用存储在哈希表中。然后检查链表 B 中的每一个结点 bib_ibi​ 是否在哈希表中。若在，则 bib_ibi​ 为相交结点。

复杂度分析
----------

时间复杂度 : O(m+n)

空间复杂度 : O(m) 或 O(n)