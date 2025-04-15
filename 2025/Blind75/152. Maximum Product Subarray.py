class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min1, max1, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            min2 = min(nums[i], max1*nums[i], min1*nums[i])
            max2 = max(nums[i], max1*nums[i], min1*nums[i])
            res = max(res, max2)
            max1, min1 = max2, min2
        return res