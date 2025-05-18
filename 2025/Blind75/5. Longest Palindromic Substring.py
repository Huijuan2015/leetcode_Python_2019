class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ""
        for i in range(len(s)):
            s1 = expandFromCenter(i, i)
            s2 = expandFromCenter(i, i+1)
            if len(s1) > len(res): res = s1
            if len(s2) > len(res): res = s2
        return res