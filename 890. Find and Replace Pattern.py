class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        res = []
        def getPattern(word):
            mp = collections.defaultdict(list)
            for i, ch in enumerate(word):
                mp[ch].append(i)
            return mp
        patternmp = getPattern(pattern)
        for word in words:
            mp = getPattern(word)
            if sorted(patternmp.values()) == sorted(mp.values()):
                res.append(word)
        return res

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w] -> 当前map长度来记录
        print F(pattern)
        return [w for w in words if F(w) == F(pattern)]