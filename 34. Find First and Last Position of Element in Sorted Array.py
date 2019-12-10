class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(nums)-1
        res = [-1, -1]
        if not nums:
            return res
        # first round, find beginning
        while start < end: #不能等于，如果等于， 会stuck
            mid = (start+end) >> 1
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
                
        if nums[start] != target:
            return res
        res[0] = start
        end = len(nums)-1
        
        # second round, find ending
        # Why does this trick work? When we use mid = (i+j)/2, the mid is rounded to the lowest integer. In other words, mid is always biased towards the left. This means we could have i == mid when j - i == mid, but we NEVER have j == mid.
        while start < end:
            mid = (start+end)/2+1 # !Make mid biased to the right
            
            if target == nums[mid]:
                start = mid
            else:
                end = mid-1
        res[1] = end
        return res