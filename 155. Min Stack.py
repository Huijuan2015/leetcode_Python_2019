class MinStack:

def __init__(self):
    self.q = []

# @param x, an integer
# @return an integer
def push(self, x):
    curMin = self.getMin()
    if curMin == None or x < curMin:
        curMin = x
    self.q.append((x, curMin));

# @return nothing
def pop(self):
    self.q.pop()


# @return an integer
def top(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][0]


# @return an integer
def getMin(self):
    if len(self.q) == 0:
        return None
    else:
        return self.q[len(self.q) - 1][1]

//use python method min
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        #self.heapq #O(n) nlgn
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.arr:
            self.arr.pop()
        else:
            return

    def top(self):
        """
        :rtype: int
        """
        if self.arr:
            return self.arr[-1]
        else:
            return

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.arr)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()