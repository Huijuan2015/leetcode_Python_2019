O(n²)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0
        def expandFromCenter(i, j):
            if i < 0 or j < 0 or j >= len(s) or i >= len(s) or s[i] != s[j]:
                return
            if s[i] == s[j]:
                self.res += 1
            return expandFromCenter(i-1, j+1)
        for i in range(len(s)):
            expandFromCenter(i, i)
            expandFromCenter(i, i+1)
        return self.res
            
DP
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count  = 0
        for length in range(1, n+1): #子串长度
            for i in range(n-length+1):
                j = i+length-1 #找子串长度是length的是不是回文串
                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    count +=1
        return count