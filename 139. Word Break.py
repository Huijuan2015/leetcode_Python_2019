class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        n = len(s)
        dp = [False for _ in range(n+1)] # dp[i] 是不是一个true 分割
        wordDict = set(wordDict)
        dp[0] = True
        for i in range(n): #s[i] , dp[i+1]
        要判断当前是不是有效位， 就去scan去前面所有有效位，看是有会有效
            for j in range(i+1): #dp坐标 ， 可以另外定义一个array 只存结果为true的值
                if dp[j]:# True
                    tmp = s[j:i+1]
                    if tmp in wordDict:
                        dp[i+1] = True
        return dp[n]
            