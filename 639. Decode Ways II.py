class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        https://blog.csdn.net/caijhBlog/article/details/78893466
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        # i = 0: 
            #i-1 == 1/2 => +=dp[i]
            #i-1= *=> 表示1、2, += 2*dp[i]
        
        # i = *:
            # += 9*dp[i-1]
            # i-1 = 1/2 => 1: += dp[i-1]*9; 2: dp[i-1]*6
            # i-1 =*: + dp[i-1]*15 (1/2)
        #i == 1~9:
            # += dp[i-1](单独)
            # i-1 = 1 => +=dp[i-1]
            # i-1 = 2 => i<=6 => +=dp[i-1]
            # i-1 = * => 
                # i<=6 => 只有当 i-1=1/2 => +=2* dp[i-1]
                # i>6 => 只有当i-1=1 => +=dp[i-1] 
        
        for i in range(len(s)):
            if s[i] == '0':
                if i-1>=0 and (s[i-1] == '1' or s[i-1] == '2'):
                    dp[i+1] += dp[i-1] 
                if i-1>=0 and s[i-1] == '*':
                    dp[i+1] += 2*dp[i-1]
            elif s[i] == '*':
                dp[i+1] += 9*dp[i]
                if i-1>=0 and s[i-1] == '1':
                    dp[i+1] += 9*dp[i-1]
                elif i-1>=0 and s[i-1] =='2':
                    dp[i+1] += 6*dp[i-1]
            else:
                dp[i+1] += dp[i]
                if i-1>=0 and s[i-1] == '1':
                    dp[i+1] += dp[i-1]
                elif i-1>=0 and s[i-1] =='2' and int(s[i]) <= 6:
                    dp[i+1] += dp[i-1]
                elif i-1>=0 and s[i-1] == '*':
                    if int(s[i]) <= 6:
                        dp[i+1] += 2*dp[i-1]
                    else:
                        dp[i+1] += dp[i-1]
        return dp[len(s)]

            