class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        alphabets = "abcdefghijklmnopqrstuvwxyz" #string.ascii_lowercase
        curr = {beginWord}
        
        dist = 1
        while curr:
            wordList -= curr
            next = set()
            for word in curr:
                for i in range(len(word)):
                    for c in alphabets:
                        tmp = word[:i]+c+word[i+1:]
                        if tmp == endWord:
                            return dist+1
                        if tmp in wordList:
                            next.add(tmp)
            curr = next
            dist+=1
        return 0


def ladderLength(beginWord, endWord, wordList):
    queue = [(beginWord, 1)]
    visited = set()
    
    while queue:
        word, dist = queue.pop(0)
        if word == endWord:
            return dist
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                tmp = word[:i] + j + word[i+1:]
                if tmp not in visited and tmp in wordList:
                    queue.append((tmp, dist+1))
                    visited.add(tmp)
    return 0