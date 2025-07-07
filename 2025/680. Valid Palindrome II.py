class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(string):
            return string  == string[::-1]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 尝试跳过左边或右边一个字符
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
        return True