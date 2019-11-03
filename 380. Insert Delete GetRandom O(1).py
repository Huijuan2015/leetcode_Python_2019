class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.nums = []
        self.d = defaultdict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.nums.append(val)
        self.d[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        #将val与最后一个数字调换，然后pop最后一个数字
        if val in self.d:
            idx = self.d[val]
            lastNum = self.nums[-1]
            self.nums[-1], self.nums[idx] = self.nums[idx], self.nums[-1]
            self.d[lastNum] = idx
            self.nums.pop() # pop last item, O(1)
            self.d.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random

        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()