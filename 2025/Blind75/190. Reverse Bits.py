class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            # 将 result 左移 1 位，为下一个位腾位置
            res <<= 1
            # 从最低位开始，每次取出 n 的最后一位（n & 1）
            # 将 n 的最低位添加到 res 的最低位上。
            # 这是 位与 运算。
	        # 1 的二进制是：000...0001
	        # 无论 n 是多少，只保留它的最低位，其余位置为 0。
            res |= (n & 1)
            # n 右移 1 位，处理下一位
            n >>= 1
        return res