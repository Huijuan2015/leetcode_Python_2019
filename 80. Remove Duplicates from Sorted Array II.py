class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <=2:
            return len(nums)
        loc = 2
        for idx in range(2, len(nums)):
            print idx, loc
            if not (nums[loc-1] == nums[idx] and nums[loc-1] == nums[loc-2]): # # move loc的条件
                nums[loc] = nums[idx]
                loc += 1
            
        return loc
                    
                    