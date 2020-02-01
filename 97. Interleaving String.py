class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #dp[i][j] : 0~i, 0~j 可以组成k: i+j+1
        # k-1: i+j
        # dp[i-1][j] and s1[i-1] == s3[i+j]
        # or dp[i][j-1] and s2[j-1] == s3[i+j]
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                elif j == 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                elif (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
        # print dp
        return dp[-1][-1]