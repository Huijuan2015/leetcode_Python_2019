class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            res = max(curr, res)
        return res