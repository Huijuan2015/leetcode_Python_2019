class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        while(low <= high):
            mid  =  low + (high-low)/2
            print (low, high, mid)
            if (mid+1 < len(A) and mid-1 >= 0 and A[mid] > A[mid+1] and  A[mid] > A[mid-1]) or mid == 0 or mid+1 == len(A):
                return mid
            if A[mid] > A[mid-1]:
                low = mid+1
            else:
                high = mid-1
        return -1