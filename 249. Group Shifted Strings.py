class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # pattern = [_ for _ in range(len(strings))]
        patterns = {}
        for string in strings:
            p = ""
            for i in range(1, len(string)):
                p += str((26+ord(string[i])-ord(string[i-1]))%26)
            if p not in patterns:
                patterns[p] = [string]
            else:
                patterns[p].append(string)
        return patterns.values()