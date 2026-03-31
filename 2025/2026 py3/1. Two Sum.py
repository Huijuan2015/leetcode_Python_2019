class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #{3,3,2}
        mp = {} # num:i
        for i, num in enumerate(nums):
            find = target - num
            if find in mp and mp[find] != i:
                return [i, mp[find]]
            mp[num] = i
        return