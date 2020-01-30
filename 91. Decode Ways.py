class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i]: 到i可以组成多少种
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1 #初始是1个数字不为0，有1种方法
        for i in range(1, n+1):
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]
            if i-2 >= 0 and (int(s[i-2]) == 1 or (int(s[i-2]) == 2 and int(s[i-1]) < 7)):
                dp[i] += dp[i-2]
        return dp[n]
                

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