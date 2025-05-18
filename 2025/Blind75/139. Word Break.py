class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 定义 dp[i] 表示：字符串前 i 个字符 s[0..i-1] 是否可以被拆分成字典中的单词。
        # 对于每个位置 i，我们检查 s[j:i] 是否在字典中，且 dp[j] 是 True，那么 dp[i] = True。
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]