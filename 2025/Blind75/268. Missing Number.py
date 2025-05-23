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


    # a ^ a = 0
    # a ^ 0 = a
    # 我们可以把所有 索引 和所有 数组里的数 都异或起来，这样：
    # • 相同的数字会互相抵消变成 0
    # • 只剩下那个缺失的数字