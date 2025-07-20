class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #以当前ch为起点，后面的string是不是palindrome
        res = 0
        # s = list(s)
        def isPanlindrome(substring):
            return substring == substring[::-1]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if isPanlindrome(sub):
                    res += 1
        return res

