class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     我们需要同时记录：
    #     • 到当前位置为止的最大乘积 max_product
    #     • 到当前位置为止的最小乘积 min_product

    # 然后根据当前值更新：
    #     • max_product = max(num, num * max_product, num * min_product)
    #     • min_product = min(num, num * max_product, num * min_product)
        if not nums:
            return 0
        maxProd = minProd = res = nums[0]

        for i in range(1, len(nums)):
            currMax = maxProd
            maxProd = max(nums[i], nums[i] * maxProd, nums[i] * minProd)
            minProd = min(nums[i], nums[i] * currMax, nums[i] * minProd)
            res = max(res, maxProd)
        return res


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