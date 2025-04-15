class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        maxInt = 2**31 - 1

        while b != 0:
            sum = (a ^ b) & mask # XOR获取不带进位的加法结果
            carry = (a & b) & mask # AND获取进位
            a = sum
            b = carry << 1 # 将进位左移一位

        # 如果结果超过 32 位整数的最大值，需要对负数进行调整
        return a if a <= maxInt else ~(a ^ mask)