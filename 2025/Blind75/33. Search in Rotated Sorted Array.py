class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # • 哪一半是有序的
        # • 目标 target 是否落在有序的这一半中
        start, end = 0, len(nums)-1
        # 我们查找的是一个确切的目标（不是区间），必须确保每一个元素都能被检查到。
        # 如果用 start < end，最后两个数只剩一个时，会直接跳出循环，漏掉最后一个数。
        # ex: nums = [4] target = 4, start == end == 0 时，应该检查这个唯一的数。
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            # 左半边是有序的
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid -1 # 已经检查了 mid 并且发现它不是目标值，所以要跳过它
                else:
                    start = mid + 1
            # 右半边是有序的
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

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

