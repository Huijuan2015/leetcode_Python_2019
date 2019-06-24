class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
--------1--------
        start=0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)/2
            if start == end:
                return start
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid
        return -1
        
--------2--------
        start=0
        end = len(nums)-1
        while start < end:
            mid = (start + end)/2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid - 1
        return start

