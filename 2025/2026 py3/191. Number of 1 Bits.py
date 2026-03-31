class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n&(n-1) #与小1的数可以消掉最右边的1
            count += 1
        return count