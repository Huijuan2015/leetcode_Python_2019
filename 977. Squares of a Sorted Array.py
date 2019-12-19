class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, k = 0, len(A)-1, len(A)-1
        res = [_ for _ in range(len(A))]
        
        while k >= 0:
            if A[i]**2 > A[j]**2:
                res[k] = A[i]**2
                i += 1
            else:
                res[k] = A[j]**2
                j -= 1
            k -= 1
        return res

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, k = 0, len(A)-1, len(A)-1
        res = [_ for _ in range(len(A))]
        
        while k >= 0:
            if A[i]*A[i] > A[j]*A[j]:
                res[k] = A[i]*A[i]
                i += 1
            else:
                res[k] = A[j]*A[j]
                j -= 1
            k -= 1
        return res