O(n) swap:
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.now = nums[:]
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.now = self.nums[:] # list(self.nums) also create new array
        return self.now

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in xrange(len(self.now) - 1):
            idx = random.randint(i,len(self.now) - 1)
            self.now[i],self.now[idx] = self.now[idx],self.now[i]
        
        return self.now


O(n^2)

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = list(self.array)
        for i in range(len(self.array)):
            idx = random.randrange(len(tmp))
            self.array[i] = tmp.pop(idx)
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()