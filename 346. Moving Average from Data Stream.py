class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []
        self.sum = 0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        #要返回平均数
        if len(self.queue) < self.size: #未满
            self.queue.append(val)    
        else:
            self.sum -= self.queue[0]
            del self.queue[0]
            self.queue.append(val)
        self.sum += val
        return float(self.sum)/len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



或者用dequeue

import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)