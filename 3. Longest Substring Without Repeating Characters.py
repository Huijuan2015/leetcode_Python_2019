class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        #left and right pointers
        #扩展right: not in visited, 记录curr length
        #update res: max(res, curr)
        #缩小left: remove visited 直到找到right
        if not s:
            return 0
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] not in visited :
                visited.add(s[right])
            else:
                while s[left] != s[right] :
                    visited.remove(s[left])
                    left += 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

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