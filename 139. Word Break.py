class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        curr = set()
        curr.add(-1)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)):
            for j  in curr:
                w = s[j+1:i+1]
                if dp[j+1] and w in wordDict:
                    curr.add(i)
                    dp[i+1] = True
                    break
        return dp[-1]
        

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        #dp: 每个字母是否可以作为单词的终结
        # a set : 当前字母之前所有可以作为终结的字母坐标
        # 每次遍历这个set，看之后所组成的新词是都在dict里
        n = len(s)
        dp = [False for _ in range(n)]
        curr = set()
        curr.add(-1)
        for i in range(n): 
            for j in curr:
                newWord = s[j+1:i+1]
                if (j == -1 or dp[j])and newWord in wordDict:
                    dp[i] = True
                    curr.add(i)
                    break 
        return dp[n-1]


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
            