class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #理论和-实际和
        n = len(nums)
        expect_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expect_sum-actual_sum


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #x ^ x = 0（任何数和自己异或等于 0）
        # x ^ 0 = x（任何数和 0 异或等于自己）
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num #所有数和坐标亦或，最后落单的一个
        return res