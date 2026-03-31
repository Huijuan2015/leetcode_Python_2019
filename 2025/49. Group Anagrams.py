class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mp = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            mp[key].append(str)
        return mp.values()