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
        curr = {beginWord} #set是dict 类型
        
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


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        q = collections.deque()
        q.append((beginWord, 1))
        visited = set()
        wordList = set(wordList)
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+ch+word[i+1:]
                    if newWord in wordList and newWord not in visited:
                        q.append((newWord, dist+1))
                        visited.add(newWord)
        return 0

        
            
        
        
                
            
        