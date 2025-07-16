class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        res = []
        for c in order:
            res.append(c * count[c])
            count[c] = 0
        for c in count:
            res.append(c * count[c])
        return ''.join(res)