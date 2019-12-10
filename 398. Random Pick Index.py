class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        from collections import defaultdict
        self.mp = defaultdict(list)
        for i, num in enumerate(nums):
            self.mp[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        n = len(self.mp[target])
        return self.mp[target][random.randint(0,n-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)