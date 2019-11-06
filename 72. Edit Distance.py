class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[_ for _ in range(l2+1)] for _ in range(l1+1)]
        dp[0][0] = 0          
        for i in range(1, l1+1):
            dp[i][0] = i
            for j in range(1, l2+1):
                print i,j
                dp[0][j] = j
                if word1[i-1] != word2[j-1]: #
                    #取 insert, remove, replace 
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
                else:
                    dp[i][j] = dp[i-1][j-1]   
        return dp[-1][-1]