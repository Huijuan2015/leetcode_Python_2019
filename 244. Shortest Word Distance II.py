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



class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # self.words = words
        self.mp = collections.defaultdict(list)
        # self.mp = {}
        self.length = len(words)
        for i, w in enumerate(words):
            # self.mp[w] = self.mp.get(w, []) + [i]
            self.mp[w].append(i)
        print self.mp

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.mp[word1]
        l2 = self.mp[word2]
        i = j = 0
        ans = self.length
        while i < len(l1) and j < len(l2):
            ans = min(ans, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


TLE: xxxxxx
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = len(self.words) + 1
        w1 = w2 = -1
        for i,word in enumerate(self.words):
            if word == word1 :
                w1 = i
            if word == word2:
                w2 = i
            if w1>=0 and w2>= 0:
                ans = min(ans, abs(w1-w2))
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)