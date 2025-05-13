class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            res[i] = temp
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            res[i] *= temp
        return res

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        tmp = 1
        for i in range(len(nums)-2,  -1, -1):
            tmp *= nums[i+1]
            res[i] *= tmp
        return res

