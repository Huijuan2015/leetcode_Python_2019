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