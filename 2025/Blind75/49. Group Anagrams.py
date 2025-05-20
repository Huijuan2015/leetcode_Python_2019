class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        mp = defaultdict(list)
        res = []
        for s in strs:
            # sorted(string)返回一个排序后的字符列表（不是字符串）
            key = ''.join(sorted(s)) #O(K log K)
            mp[key].append(s)
        for k, v in mp.items():
            res.append(v)
        return res


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