from math import ceil
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        m = int(ceil(len(B)/float(len(A))))
        
        if B in A*m:
            return m
        elif B in A*(m+1):
            return m+1
        elif B in A*(m+2):
            return m+2
        return -1