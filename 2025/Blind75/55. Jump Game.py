class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, nums[i]+i)
            else:
                return False
        return True
