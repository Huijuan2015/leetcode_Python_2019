class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end =  len(nums) - 1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid -1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

要学习
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start <= end: # 找特定的值要return 需要等于
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]: # normal order
                if target < nums[mid] and target >= nums[start]:
                    end = mid-1
                else:
                    start = mid+1
            else: # rotate
                if target <= nums[end] and target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1

