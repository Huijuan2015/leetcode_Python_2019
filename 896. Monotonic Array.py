class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        #1. python sorted nlogn
        return sorted(A) == A or sorted(A, reverse=True) == A
        
        #2. for
        if not A or len(A) <= 1:
            return True
        increase = True
        if A[0] > A[1]:
            increase = False
        for i in range(1, len(A)):
            if (increase and A[i] < A[i-1]) or (not increase and A[i] > A[i-1]):
                return False
        return True
                
                
            