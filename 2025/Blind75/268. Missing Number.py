class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i^n
        return missing

# XOR（异或）是一种按位运算。
# 当两个值不同时，输出为真（即为1），例如：
# 1^0 = 1，1^1 = 0，2^0 = 2，2^2 = 0。
# 一个值与自身异或的结果是0。
# XOR 运算是可交换的
# 1^1^2 == (1^1)^2 == (2^1)^1 == 2