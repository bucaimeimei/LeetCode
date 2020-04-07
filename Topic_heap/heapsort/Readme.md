#堆排序
========

堆排序思想：
---------

1. 首先将待排序的数组构造出一个大根堆

2. 取出这个大根堆的堆顶节点(最大值)，与堆的最下最右的元素进行交换，然后把剩下的元素再构造出一个大根堆

3. 重复第二步，直到这个大根堆的长度为1，此时完成排序。

编码主要解决的问题：
-----------------

如何把一个序列构造出一个大根堆

输出堆顶元素后，如何使剩下的元素构造出一个大根堆

python实现：
----------


from collections import deque

L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])

def heap_sort(L):

    L_length = len(L) - 1

    first_sort_count = L_length / 2
    
    for i in range(first_sort_count):
    
        heap_adjust(L, first_sort_count - i, L_length)
        

    for i in range(L_length - 1):
    
        L = swap_param(L, 1, L_length - i)
        
        heap_adjust(L, 1, L_length - i - 1)
        

    return [L[i] for i in range(1, len(L))]
    











