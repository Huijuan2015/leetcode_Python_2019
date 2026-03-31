class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #如果一个数是 2 的幂，它的二进制表示中有且仅有一个 1，其余位全是 0（且该数必须大于 0）
        #排除负数和0
        return n > 0 and (n&(n-1)) == 0