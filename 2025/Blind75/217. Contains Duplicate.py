class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sort O(nlogn)
        # set or map space O(n)
        return len(set(nums)) != len(nums)
