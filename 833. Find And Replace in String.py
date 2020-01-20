class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

        # indexes = sorted(indexes, reverse=True)
        # 
        为了保证S后面没有被改变， 要从后往前替换
        需要给三个数组对应排序
        for idx, source, target in sorted(zip(indexes, sources, targets), reverse = True):
            l = len(source)
            if idx+l <= len(S) and S[idx:idx+l] == source:
                S = S[:idx] + target + S[idx+l:]
                # print S
        return S