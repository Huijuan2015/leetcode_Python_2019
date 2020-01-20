class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, last = len(nums)-1, len(nums)-1
        while i >= 0: #从后往前看是否到达idx 0
            if i + nums[i] >= last:
                last = i
            i -= 1
        return last == 0
            