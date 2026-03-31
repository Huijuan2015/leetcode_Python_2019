class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1 #左移 从后
            res += (n & 1) # n&1 n的最后一位， res = res | (n&1)
            n = n >> 1 #右移 从前
        return res
