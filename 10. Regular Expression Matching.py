class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] s[i]与p[j]匹配与否
        # s[i]==p[j] or p[j] = '.' > dp[i][j] = dp[i-1][j-1]
        # s[i]!=p[j] and p[j] == '*': (p[j] = * or False):
        #         p[j] = 0/1/2~n:
        #             1. p[i-1] = s[i] or p[i-1] = '.': 0 or 1 or n:
        #                     dp[i][j] = dp[i][j-2] || dp[i-1][j-1] || dp[i-1][j]
        #             2. dp[i][j] = dp[i][j-2] (p[i-1]=* and *=0)
        
        m, n = len(s), len(p)
        
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        # dp[0][j] p从第二位开始都是*
        for j in range(1, n):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True
                
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    # print m, n, i+1, j+1
                    # print dp, dp[i+1][j+1], 
                    dp[i+1][j+1] = dp[i][j]
                elif j-1>=0 and s[i] != p[j] and p[j] == '*':
                    if (s[i] == p[j-1] or p[j-1] == '.'):
                        dp[i+1][j+1] = dp[i+1][j-1] or dp[i][j] or dp[i][j+1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
        return dp[-1][-1]
        
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
        #s[i-1] != p[i-1] and p[i-1]== *)  => p[j-1] == '*'
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
                    