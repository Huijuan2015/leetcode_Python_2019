class WordDistance(object):
    # dict = {}
    def __init__(self, words):
        """
        :type words: List[str]
        """
        # self.dict = {}
        # for i, n in enumerate(words):
        #     self.dict[n] = self.dict.get(n, []) + [i]
            
        self.dict = collections.defaultdict(list)
        for i in range(len(words)):
            self.dict[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = sys.maxsize
        idx1 = -1
        idx2 = -1
        i = j = 0
        while i < len(self.dict[word1]) and j < len(self.dict[word2]):
            res = min(res, abs(self.dict[word1][i] - self.dict[word2][j]))
            if self.dict[word1][i] < self.dict[word2][j]:
                i += 1
            else:
                j += 1
        
        return res 


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)