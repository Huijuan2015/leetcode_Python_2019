class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sort O(nlogn)
        # set or map space O(n)
# 总时间复杂度：O(n)
# 空间复杂度：O(n)（用来存储临时的 set(nums)）
        return len(set(nums)) != len(nums)

