class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #left, right sum without the num
        left, right = [0]*len(nums), 0
        res = -1
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
        if left[-1] == 0:
            res = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            right += nums[i+1]
            if right == left[i]:
                res = i
        return res


数学计算法
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # l = r
        # r = total - l - nums[i]
        # l = total - l - nums[i]
        # 2l+nums[i] = total
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == (total - left - x):
                return i
            left += x
        return -1