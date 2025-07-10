class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right+left)//2
            if nums[mid] > nums[mid+1]: #left has peak
                right = mid
            else:
                left = mid+1
        return left # 最后收敛成一个点的时候，那就是一个峰值
