class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = -1
        idx2 = -1
        res = len(words)
        for i in xrange(len(words)):
            tmp =  len(words)
            if words[i] == word1:
                idx1 = i
            if words[i]  == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                tmp = abs(idx1-idx2)
            res = min(tmp, res)
            
        return res 
                

class Solution(object):
    
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        w1 = w2 = -1
        ret = len(words) + 1
        for i in range(len(words)):
            if words[i] == word1:
                w1 = i
            elif words[i] == word2:
                w2 = i
            if w1>=0 and w2>= 0:           
                ret = min(ret,abs(w1-w2))
        return ret
            
                