class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp[i][j] s[i~j] 是不是PS
        # 1> dp[i+1][j-1]
        # 2> s[i] = s[j]
        # or j-i <= 2
        # i < j 右上角
        if not s or len(s) < 2:
            return s
        n = len(s)
        start, end = 0, 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in reversed(range(n-1)):# 0~end-1
            for j in range(i+1, n): #i+1~end 确保j在i右边
                if (dp[i+1][j-1] or j-i<=2) and s[i]==s[j]:
                    dp[i][j] = True
                    if j-i+1 > end-start+1:
                        start = i
                        end = j
        return s[start:end+1]
        
                
        