双栈会超时，这题用双向链表做

class MaxStack:

    def __init__(self):
        self.stk = []
        self.max_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.max_stk or x >= self.max_stk[-1]:
            self.max_stk.append(x)
        else:
            self.max_stk.append(self.max_stk[-1])

    def pop(self) -> int:
        self.max_stk.pop()
        return self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.max_stk[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        # 要找到stk中的latest最大然后删除
        buffer = []
        while self.top() != max_val:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()