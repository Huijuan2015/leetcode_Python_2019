class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s):
            return s == s[::-1] #o(n)
        
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start] != s[end]:
                return isValid(s[start:end]) or isValid(s[start+1:end+1])
            start += 1
            end -= 1
        return True


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0 # count <= 1
        start  = 0
        end  = len(s)-1
        while start < end:
            if s[start] != s[end]:
                count += 1
                if count > 1:
                    return False
                else:
                    start1, start2, end1, end2 = start+1, start, end, end-1
                    while (start1 < end1 and s[start1] == s[end1]):
                        start1 += 1
                        end1 -= 1
                    while (start2 < end2 and s[start2] == s[end2]):
                        start2 += 1
                        end2 -= 1
                    return start1 >= end1 or start2 >= end2
            else:
                start += 1
                end -= 1
        return True