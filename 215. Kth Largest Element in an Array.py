class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sort nlogn
        # return sorted(nums, reverse = True)[k-1]
    
        # heap sort
        return heapq.nlargest(k,nums)[-1]  #O((n-k) log n) = O(n log n) O(n) extra space.
        # partition 
        if k < 0 or k > len(nums):
            return
        start = 0
        end = len(nums) - 1
        mid = self.partition(nums, start, end)
        key = len(nums) - k
        while mid != key:
            if mid < key:
                mid = self.partition(nums,mid+1, end)
            else:
                mid = self.partition(nums,start, mid-1)
        return nums[mid]
    
    def partition(self, nums, start, end):
        pivot = nums[start]
        while start < end:
            while start < end and nums[end] >= pivot:
                end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] <= pivot:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        return start

heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapq o(n) extra space
        import heapq # smallest
        n = len(nums)
        heapq.heapify(nums)  # O(n)
        # print (list(nums)) 
        
        while n-k > 0:
            heapq.heappop(nums)
            k += 1
        return heapq.heappop(nums)

