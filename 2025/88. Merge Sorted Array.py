class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        tail = m+n-1
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            n1 = nums1[i] 
            n2 = nums2[j]
            if n1 >= n2:
                nums1[tail] = n1
                i -= 1
            else:
                nums1[tail] = n2
                j -= 1
            tail -= 1
        while i >= 0:
            nums1[tail] = nums1[i]
            tail -= 1
            i -= 1
        while j >= 0:
            nums1[tail] = nums2[j]
            tail -= 1
            j -= 1
        return nums1


