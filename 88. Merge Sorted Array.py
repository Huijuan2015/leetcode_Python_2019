class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        k = m+n-1
        
        while k >= 0:
            if n-1<0 or (m-1 >= 0 and nums1[m-1]>=nums2[n-1]):
                nums1[k] = nums1[m-1]
                m -= 1
            elif m-1 < 0 or (n-1>=0 and nums1[m-1]<nums2[n-1]):
                nums1[k] = nums2[n-1]
                n -= 1
            k-=1
        


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        i, j = m-1, n-1
        while k >= 0:
            if j < 0:
                break
            if i < 0:
                nums1[:k+1] = nums2[:j+1]
                break
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        # return


        
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 2 pointer insert? not working, cannot create new space
        # m + n
        # i, j = 0, 0
        # while j < n:
        #     if nums2[j] >= nums1[i]:
        #         nums1.insert(i+1,nums2[j])
        #         j += 1
        #         i += 1
        #     i += 1
            
        # return nums1[:m+n] 
        
        # 2 point from back to beginning
        i, j, k = m-1, n-1, m+n-1
        while i >=0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        # while j >= 0:
        #     nums1[k] = nums2[j]
        #     j -= 1
        #     k -= 1