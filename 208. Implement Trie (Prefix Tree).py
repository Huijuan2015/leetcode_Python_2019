class TrieNode():
    def __init__(self):
        self.letters = [None for _ in range(26)]
        self.isWord = False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for ch in word:
            if not curr.letters[ord(ch)-ord('a')]:
                curr.letters[ord(ch)-ord('a')] = TrieNode()
            curr = curr.letters[ord(ch)-ord('a')]

        curr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if curr.letters[ord(ch)-ord('a')]:
                curr = curr.letters[ord(ch)-ord('a')]
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if curr.letters[ord(ch)-ord('a')]:
                curr = curr.letters[ord(ch)-ord('a')]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)