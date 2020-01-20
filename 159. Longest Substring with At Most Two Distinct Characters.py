class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, second = -1, -1
        i = 0
        res = 0
        while i < len(s):
            if first == -1:
                first = i
            elif second == -1 and s[first] != s[i]:
                second = i   
            elif s[i] != s[first] and s[i] != s[second]: # 当s[i] 是第三个数时， 第一个数拉到第二个数，第二个数重新计算（abaccc)
                first = second
                second = -1 # second要拉回-1
                i = first
            res = max(res, i-first+1)
            i += 1
        return res

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
            
            
                
                