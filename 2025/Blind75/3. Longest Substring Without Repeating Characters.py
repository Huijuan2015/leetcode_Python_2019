class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #left and right pointers
        #扩展right: not in visited, 记录curr length
        #update res: max(res, curr)
        #缩小left: remove visited 直到找到right
        visited = set()
        if not s:
            return 0
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
            else: #移除直到重复出现的char
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
