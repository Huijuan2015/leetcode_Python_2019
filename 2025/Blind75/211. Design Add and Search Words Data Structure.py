class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = TrieNode()
                node = node.children[ch]
        node.isWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
        
        # need to bypass . and do search
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            if word[0] not in node.children:
                return
            self.dfs(node.children[word[0]], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)