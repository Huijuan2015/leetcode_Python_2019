class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = collections.Counter(s)
        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        dic = Counter(s)
        # for i, v in enumerate(s):
        #     dic[v] += 1s
        for i, v in enumerate(s):
            if dic[v] == 1:
                return i
            
        return -1