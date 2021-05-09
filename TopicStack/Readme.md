#### 栈：FILO
    后存储，先出来的一种数据结构
    栈顶标记:top标记栈顶元素位置
    常用操作：
        入栈
        出栈
        获取栈顶元素
        判断栈是否为NULL
    实现方式：
    数组栈
    链式栈

#### 面试题 03.02. 栈的最小值

    请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。
    执行push、pop和min操作的时间复杂度必须为O(1)。

    示例：

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.

#### 解题思路
1.双栈法
----------

![image](https://user-images.githubusercontent.com/42366181/117565518-4a44ff80-b0e4-11eb-8492-f6621b38d645.png)
![image](https://user-images.githubusercontent.com/42366181/117565534-5761ee80-b0e4-11eb-8692-d9d918a3f7be.png)
![image](https://user-images.githubusercontent.com/42366181/117565562-7a8c9e00-b0e4-11eb-9463-9133de2db8bd.png)
![image](https://user-images.githubusercontent.com/42366181/117565575-86786000-b0e4-11eb-8bf9-e7070d72d2be.png)
![image](https://user-images.githubusercontent.com/42366181/117565592-985a0300-b0e4-11eb-8e5f-41fc1de3b182.png)
![image](https://user-images.githubusercontent.com/42366181/117565597-a4de5b80-b0e4-11eb-99c0-aedf319be96f.png)
![image](https://user-images.githubusercontent.com/42366181/117565613-b889c200-b0e4-11eb-8435-7f9f301da59b.png)
![image](https://user-images.githubusercontent.com/42366181/117565622-c4758400-b0e4-11eb-869e-91b3161f198c.png)
![image](https://user-images.githubusercontent.com/42366181/117565865-2682b900-b0e6-11eb-9a3a-9109eac55816.png)
![image](https://user-images.githubusercontent.com/42366181/117563277-51194580-b0d7-11eb-8f37-5c630a9cb01c.png)


    class MinStack:
    
        def __init__(self):
            self.stack = []
            self.min_stack = [math.inf]

        def push(self, x: int) -> None:
            self.stack.append(x)
            self.min_stack.append(min(x, self.min_stack[-1]))

        def pop(self) -> None:
            self.stack.pop()
            self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]
        

2.单栈法
----------

![image](https://user-images.githubusercontent.com/42366181/117566158-9ba2be00-b0e7-11eb-8b1d-733d97d6f61d.png)
![image](https://user-images.githubusercontent.com/42366181/117566168-a9584380-b0e7-11eb-8d1f-58821cb74d7d.png)
![image](https://user-images.githubusercontent.com/42366181/117566177-b37a4200-b0e7-11eb-920b-497e64afe175.png)
![image](https://user-images.githubusercontent.com/42366181/117566193-cf7de380-b0e7-11eb-9f2a-ba1f6a22175f.png)

    class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        min_num = self.stack[-1][1]   if self.stack else  None
        if min_num is None:
            self.stack.append((x,x))
        elif x<=min_num:
            self.stack.append((x,x))
        elif x>min_num:
            self.stack.append((x,min_num))


    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
         return self.stack[-1][1]
