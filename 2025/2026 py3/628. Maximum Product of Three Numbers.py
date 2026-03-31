class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #sort, max 3 or min2*max1
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])