class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        curr = ret
        for num in nums[1:]:
            curr = max(num, curr + num)
            ret = max(ret, curr)
        return ret