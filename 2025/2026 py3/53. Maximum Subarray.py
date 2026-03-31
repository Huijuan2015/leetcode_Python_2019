class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        start, curr, res = 0, 0, float('-inf')
        for i in range(len(nums)):
            if nums[i] >= curr + nums[i]:
                start = i
                curr = nums[start]
            else:
                curr += nums[i]
            res = max(res, curr)
        return res
dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        max_sum = nums
        # 以当前位置结尾的连续子数组所能达到的最大和
        for i in range(1, len(nums)):
            if max_sum[i-1] > 0: #只有当时正数的时候才吸收进来，也可以用同一个nums数组做原地计算
                max_sum[i] = max_sum[i-1] + nums[i]
        return max(max_sum)

