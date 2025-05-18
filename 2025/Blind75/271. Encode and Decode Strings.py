class Codec:
    # 对于每个字符串 s，我们将其编码为：长度 + '#' + s
    # ["hello", "world"] → "5#hello5#world"
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#': #length
                j += 1
            length = int(s[i:j])
            j = j + 1 # skip '#'
            res.append(s[j:j+length])
            i = j+length   
        return res

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))