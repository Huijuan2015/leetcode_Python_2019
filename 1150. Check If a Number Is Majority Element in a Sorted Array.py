class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # find left start and check left+n/2
        
        first = self.findLeft(nums, target)
        last = first+len(nums)/2
        if last < len(nums) and nums[first] == target and nums[last] == target:
            return True
        return False
    
    def findLeft(self, nums, target):
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid
        return start