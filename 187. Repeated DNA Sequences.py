class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 10:
            return
        dna = set()
        res = set()
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in dna:
                res.add(curr)
            dna.add(curr)     
        return list(res)