# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def compare(w1, w2):
            # 对应位上相同才算相同
            return sum(1 for c1, c2 in zip(w1, w2) if c1 == c2)
        
        oldList = wordlist
        n = 0
        while n < 6:
            newList = []
            更好的选择random word 的方法，选择 与别的单词match 为0 的最少的数， min worst case minmax
            guessedWord = random.choice(oldList)  
            n = master.guess(guessedWord)
            # newList.append(guessedWord)
            for word in oldList:
                if compare(word, guessedWord) == n:
                    newList.append(word)
            oldList = newList[:]
        
        