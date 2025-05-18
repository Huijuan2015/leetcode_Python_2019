class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0

        while n:
            n &= n - 1
            print n
            c += 1
        return c


    •   n & 1：取出最低位是否是 1（是的话加 1）
    •   n >>= 1：把 n 右移，继续处理下一位
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


    •   每次执行 n &= n - 1，都会把 最右边的一个 1 消除
    •   所以循环的次数，就是 1 的个数！
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # 这个操作会把 n 的二进制中最右边的那个 1 变成 0，其余的位保持不变。
            n &= n - 1
            count += 1
        return count