class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] -> 以i 结尾的有效长度
        n = len(s)
        dp = [0 for _ in range(n+1)]
        res = 0
        for i in range(1, n): # s:0~n-1; dp[i+1]-> s[i]结尾
            if s[i] == ')':
                if s[i-1] == ')':
                    idx = i-1 - dp[i]
                    if idx >= 0 and s[idx] == '(':
                        dp[i+1] = dp[i]+2+dp[idx]
                else:
                    dp[i+1] = dp[i-1]+2
            res = max(dp[i+1], res)
        print dp
        return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i] 0~i, 以i结尾的LVP
        #s[i]: (-> dp[i] = 0 ; 
        #s[i]: )-> 看s[i-1]
            #s[i-1]-> ): string like ...id.....))
                #find id before start of dp[i-1]
                #only if s[id] = (: dp[i] = dp[i-1]+2+dp[id-1]

            #s[i-1]-> (: string like ....()
                # dp[i] = dp[i-2] +2
        if not s or len(s) < 2:
            return 0
        n = len(s)   
        dp = [0 for _ in range(n+1)]
        ans = 0
        for i in range(2, n+1):
            if s[i-1] == ')':
                if s[i-2] == ')':
                    id = i-2 - dp[i-1]
                    if id>=0 and s[id] == '(':
                        dp[i] = dp[i-1]+2+dp[id]
                else:
                    dp[i] = dp[i-2]+2
            ans = max(ans, dp[i])
        return ans
        
        