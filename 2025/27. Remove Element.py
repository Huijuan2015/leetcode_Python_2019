class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        return curr
