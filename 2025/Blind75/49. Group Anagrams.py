class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        mp = defaultdict(list)

        for word in strs:
            tmp = ''.join(sorted(word))
            mp[tmp].append(word)
        res = []
        for tmp, words in mp.items():
            res.append(words)
        return res