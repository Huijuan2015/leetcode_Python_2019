class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #中心扩展
        self.res = 0
        def extend(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.res += 1
                left -= 1
                right += 1
        for i in range(len(s)):
            extend(i, i)
            extend(i, i+1)
        return self.res


暴力 O(n3)
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





