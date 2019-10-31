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
        end =len(nums)-1
        while start <= end:
            # mid = (start+end) / 2
            mid = (start+end) >> 1
            if nums[mid] == target:
                return mid
            # mid > start
                # start<target < mid
                # else
            # mid < start
                # mid<target<end
                # else
            if nums[mid] >= nums[start]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target  > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1