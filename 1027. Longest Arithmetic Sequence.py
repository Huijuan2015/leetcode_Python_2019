class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [dict() for _ in A]
        # print dp
        maxl = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                v = A[j]-A[i]
                if v in dp[j]:
                    dp[i][v] = dp[j][v]+1
                else:
                    dp[i][v] = 1
                maxl = max(maxl, dp[i][v])
        return maxl+1


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [dict() for _ in A]
        maxl = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                sub = A[j]-A[i]
                if sub in dp[j].keys(): -> .keys 超时
                    dp[i][sub] = dp[j][sub]+1
                else:
                    dp[i][sub] = 1
                maxl = max(maxl, dp[i][sub])
        print dp
        return maxl+1