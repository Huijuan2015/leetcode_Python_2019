class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
# string 可以包含26个字母以外的东西
        visited = set()
        low, high = 0, 0
        res = 0
        while high < len(s):
            curr = s[high]
            if curr in visited:
                # res = max(res, high-low)
                while s[low] != curr:
                    visited.remove(s[low])
                    low += 1
                low += 1
            else:
                visited.add(curr)
            每次更新
            res = max(res, high-low+1)
            high += 1
        return res