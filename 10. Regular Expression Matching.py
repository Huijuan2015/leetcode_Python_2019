class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j]: s[0:i]匹配p[0:j] true or false
        # 初始化 m+1, n+1, all false
        #dp[0][0] = true
        #dp[0][j] p从第二位开始都是* and dp[0][j-1] true
        #dp[i][0] false
        
        #s[i-1] == p[i-1] or p[i-1]=='.': dp[i][j] = dp[i-1][j-1]
        #s[i-1] != p[i-1] and p[i-1]!='.': (== *)  => p[j-1] == '*'
        #   * 代表 0/1/2~n :
        #       p[i-2] == s[i-1] or '.': 0 || 1 || 2~n
        #                dp[i][j] = dp[i][j-2] || dp[i-1][j-1] || dp[i-1][j]
        #       else: dp[i][j-2] ( abc, ad*c, *只能是0,使d消失)
        
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n):
            dp[0][j+1] = (p[j] == '*' and dp[0][j-1])  #!!!
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif j>1 and s[i-1] != p[j-1] and p[j-1] == '*': #!!!
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = (dp[i][j-2] or dp[i-1][j-1] or dp[i-1][j])
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[m][n]
                    