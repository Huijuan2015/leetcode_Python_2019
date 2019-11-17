from collections import defaultdict
class Solution(object):
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        wordList = set(wordList)
        wordList.add(beginWord)
        self.visited = {}
        mp = self.buildGraph(wordList, beginWord, endWord)
        # BFS      
        res = []
        curr = [(beginWord,[beginWord])] # word以及当前到达word的valid path
        while curr:
            next = []
            validAttempt = [] #收集当前层所有attempt，可能会有重复，最后一起置位visited
            for pair in curr:
                word, parent = pair[0], pair[1]         
                for attempt in mp[word]:
                    attemptPath = parent + [attempt]
                    if attempt == endWord:
                        res.append(attemptPath)
                    elif attempt != endWord and not self.visited[attempt]:
                        validAttempt.append(attempt)
                        next.append((attempt, attemptPath))
            for attempt in validAttempt:    
                self.visited[attempt] = True
            curr = next if not res else [] #确定找到最短path层后就不往后了
        return res
                        
                
    def buildGraph(self, wordList, beginWord, endWord):
        mp = defaultdict(set) # word:(words can chang to )
        for word in wordList:
            self.visited[word] = False
            if word == endWord:
                continue
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    tmp = word[:i]+c+word[i+1:]
                    if tmp == beginWord:
                        continue
                    elif tmp in wordList:
                        mp[word].add(tmp)
        return mp
        
        
        
        
  