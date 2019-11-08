class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        l1, l2 = len(s), len(t)

        if abs(l1-l2) > 1:#大于1
            return False
        elif abs(l1-l2) == 1: #增减1个
            i, j = 0, 0
            while i < l1 and j < l2:
                if s[i] != t[j]:
                    return s[i:] == t[j+1:] or s[i+1:]==t[j:]
                i+=1
                j+=1
                
        elif abs(l1-l2) == 0: #replace
            cnt = 0
            i, j = 0, 0
            while i < l1 and j < l2:
                if s[i] != t[j]:
                    cnt += 1
                    if cnt > 1:
                        return False
                i+=1
                j+=1
        return True