class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [2, 2, 2, 0, 2] 当 nums[mid] == nums[right] 时，我们不能判断最小值在哪边。
        # 无法判断方向，安全地将 right 左移一位。
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end-start)/2
            if nums[mid] > nums[end]:
                start  = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
            else:
                end -= 1
        return nums[start]