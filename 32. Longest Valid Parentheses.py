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
        
        