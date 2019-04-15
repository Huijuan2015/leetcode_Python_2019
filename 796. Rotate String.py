class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for i in xrange(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False