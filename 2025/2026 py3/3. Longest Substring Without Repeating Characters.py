class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return len(s)
        start, maxLen = 0, 0
        _set = set()

        for i in range(len(s)):
            if s[i] not in _set:
                _set.add(s[i])
                maxLen = max(maxLen, i-start+1)
            else:
                while s[start] != s[i]:
                    _set.remove(s[start])
                    start += 1
                start += 1
        return maxLen
