class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 即使旋转过，数组仍然可以被分成一个 有序段 + 另一个有序段。最小值一定在 无序段 中
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end-start)/2
            # 如果中间元素 > 右边界，最小值在右边
            if nums[mid] > nums[end]: # 无序段
                start = mid + 1
            else:
                end = mid
        return nums[start]
        # • 如果数组没被旋转（如 [1, 2, 3, 4]）会正常返回最左侧元素。
        # • 只有一个元素：直接返回。
                

    class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end]) #?