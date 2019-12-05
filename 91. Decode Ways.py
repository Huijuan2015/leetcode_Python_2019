class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)] #dp[i]: 0~i 有多少种可能
        dp[0] = 1 #可能有confusion
        for i in range(n): #s[i]
            if int(s[i]) != 0:
                dp[i+1] += dp[i]
            
            if i-1 >= 0 and int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) > 9:
                dp[i+1] += dp[i-1]
            
        return dp[n]