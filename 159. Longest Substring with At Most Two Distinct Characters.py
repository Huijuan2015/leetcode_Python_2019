class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, second, start = -1, -1, 0
        res = 0
        while start < len(s):
            if first == -1:
                first = start
            elif second == -1 and s[start] != s[first]:
                second = start
            elif first != second and s[start] != s[first] and s[start] != s[second]:
                # print start, first
                # res = max(res, start-first)
                first = second
                second = -1
                start = first
            res = max(res, start-first+1)    
            start += 1
        res 
        return res
            
            
                
                