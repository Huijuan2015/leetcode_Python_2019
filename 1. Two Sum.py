class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #index_map = {u: i for i, u in enumerate(A)}
        mp={u: i for i,u in enumerate(nums)}
        for i, n in enumerate(nums):
            find = target - n
            if find in mp and mp[find] != i:
                return [i,mp[find]]
        