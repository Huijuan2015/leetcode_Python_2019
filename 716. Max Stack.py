class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        currMax = x
        if self.stk:
            currMax = max(currMax, self.stk[-1][1])
        self.stk.append((x, currMax))

    def pop(self):
        """
        :rtype: int
        """
        if self.stk:
            return self.stk.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if self.stk:
            return self.stk[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        if self.stk:
            return self.stk[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        m = self.stk[-1][1]
        tmp = []
        while self.stk and self.stk[-1][0] != m:
            tmp.append(self.stk.pop())
        self.stk.pop()
        currMax = float('-inf')
        if self.stk:
            currMax = self.stk[-1][1]
        # print self.stk, tmp
        while tmp:
            x = tmp.pop()[0]
            currMax = max(currMax, x)
            self.stk.append((x, currMax))
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


2 stack
当前最大值


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.insert(0, x) # O(n) 
        # self.data.append(x) #O(1)

    def pop(self):
        """
        :rtype: int
        """
        return self.data.pop(0)
        # return self.data.pop(-1)
        
    def top(self):
        """
        :rtype: int
        """
        # return self.data[-1]
        return self.data[0]

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.data) #O(n)

    def popMax(self):
        """
        :rtype: int
        """
        val = max(self.data)
        self.data.remove(val) #O(n)
        return val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()