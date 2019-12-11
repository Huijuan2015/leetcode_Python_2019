class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # mp
        def checkOrder(w1, w2):
            mp = {u:i for i, u in enumerate(order)}
            idx2 = 0
            for idx1 in range(len(w1)):
                ch1 = w1[idx1]
                ch2 = w2[idx2]
                if mp[ch1] < mp[ch2]:
                    return True
                elif mp[ch1] > mp[ch2]:
                    print 2
                    return False
                idx2 += 1
                if idx2 >= len(w2):
                    return False
        
        if not words or len(words) < 2:
            return True
        
        prev = words[0]
        for i in range(1, len(words)):
            if not checkOrder(prev, words[i]):
                return False
            prev = words[i]
        return True
    
Hash indexes of each character for better runtime
Compare every adjacent word
If any letter of former word is in higher order, return False
If current letter of former word is in lower order, forget the rest of word
If lenght of former word is longer and latter word is substring of former, return False (apple & app etc.)
Return True        
class Solution:
    def isAlienSorted(self, words, order):
        ind = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] > ind[s2]:
                    return False
        return True                    
                
                