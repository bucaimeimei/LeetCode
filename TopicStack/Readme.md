
https://pic.leetcode-cn.com/1617197321-MBzdwF-7.jpg
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
