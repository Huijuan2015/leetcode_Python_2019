class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.d = defaultdict(set)
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.d[val].add(len(self.nums)-1)
        return len(self.d[val]) == 1   

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.d[val]:
            # self.d.pop(val)
            return False
    
        # 先在dict中找到index list set
        # 从set中找到index然后 队尾调换删除
        # 查找队尾元素在dict-value中的位置需要用到set
        idx = self.d[val].pop() #set最后一个
        if not self.d[val]:
            del self.d[val]
        # 要先删除 self.nums[idx]
        lastnum = self.nums[-1]
        lastidx = len(self.nums)-1
        #交换2个数字   
        self.nums[idx] = lastnum
        self.nums.pop()
        # 原末尾元素的set中要删除一个index并添加一个新index
        # if lastnum in self.d:  
        self.d[lastnum].add(idx)
        self.d[lastnum].remove(lastidx)
        return True  

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()