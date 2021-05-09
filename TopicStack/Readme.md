
#### 解题思路1
双栈法
stack：记录数据。 min：追踪min （单调栈）
当x == min[-1]时也要push， 因为pop处我们的逻辑是，如果pop出的元素==min[-1]，那么就代表相应元素被pop，min[-1]也要被pop，所以push的时候也要push，不然的话会出现stack有值，min中空栈的情况。 （在单调队列和单调队列中这个是普遍常识，相等元素是核心关键）

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
