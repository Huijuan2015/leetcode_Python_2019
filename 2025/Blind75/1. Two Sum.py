class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {u:i for i, u in enumerate(nums)}
        for i,n in enumerate(nums):
            find = target - n
            if find in mp and mp[find] != i:
                return [i, mp[find]]
