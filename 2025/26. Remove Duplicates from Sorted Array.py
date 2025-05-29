class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[curr] = nums[i]
                curr += 1
        return curr
