class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        用一个set保持window
        if k == 0 or not s:
            return 0
        kset = set()
        first = 0
        res = 0
        start = 0
        while start < len(s):
            if len(kset) < k:
                kset.add(s[start])
            elif len(kset) == k and s[start] not in kset:
                # 从后往前，找最先出现的first = s[start]
                kset.clear()
                first = start
                while len(kset) < k or s[first] in kset: 往前推出ksize s[first] in kset/(s[first] not in kset && len(kset) < k)
                    kset.add(s[first])
                    first -= 1
                first += 1
            res = max(res, start-first+1)
            start += 1
        return res