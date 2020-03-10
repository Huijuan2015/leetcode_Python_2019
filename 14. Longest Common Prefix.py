class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        curr = strs[0]
        for s in strs[1:]:
            curr = self.getCommon(curr, s)
            if not curr:
                return ""
        return curr
    
    def getCommon(self, s1, s2):
        if not s1 or not s2:
            return
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                break
            i += 1
            j += 1
        return s1[:i]
    