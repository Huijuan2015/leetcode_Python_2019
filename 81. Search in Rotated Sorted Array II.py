class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        start = 0
        end = len(nums)-1
        
        while start <= end:
            while start < end and nums[start] == nums[start+1]: start += 1
            while start < end and nums[end] == nums[end-1]: end -= 1
            mid = (start+end)/2
            if nums[mid] == target:
                return True
            if nums[mid]<nums[start]: #后半段 
                if target <= nums[end] and nums[mid] < target: # 确保mid<target<=end， 才可以往右缩； 需要等于可以用1，3，5举例子
                    start = mid+1
                else:
                    end = mid-1
            else:# 前半段
                if target >= nums[start] and nums[mid] > target:
                    end = mid -1
                else:
                    start = mid+1
            
        return False