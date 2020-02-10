class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, n in enumerate(nums):
            print missing, i, n
            missing ^= i^n
            print missing
        return missing


        missing = len(nums)
        for i in range(len(nums)):
            missing ^= (nums[i]^i)
        return missing