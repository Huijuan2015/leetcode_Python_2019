class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        自己定义map，不能直接用map，还需要考虑key的顺序
        def RLE(s): # return string, list
            prev = -1
            key = ""
            cnts = []
            for i in range(len(s)):
                if i== len(s)-1 or s[i] != s[i+1]:
                    key += s[i]
                    cnts.append(i-prev)
                    prev = i
            return (key,cnts)
                    
        def isExtended(skey, scnt, wkey, wcnt):
            if skey != wkey or len(skey) != len(wkey):
                return False
            for i in range(len(scnt)):
                c1, c2 = scnt[i], wcnt[i]
                if c2 > c1:
                    return False
                if c1 < 3 and c1 != c2:
                    return False
            return True
        
        skey, scnt = RLE(S)
        cnt = 0
        for word in words:
            wkey, wcnt  = RLE(word)
            if isExtended(skey, scnt, wkey, wcnt):
                cnt += 1
                # print word
        return cnt
            